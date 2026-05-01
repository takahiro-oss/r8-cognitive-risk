#!/usr/bin/env python3
"""
ailabel_claude.py — Claude API を使ったAIlabelアノテーションツール

使い方:
  python ailabel_claude.py --subset docs/design/AIlabel_subset_30.md --corpus corpus --out ailabel/results_claude.csv
  python ailabel_claude.py --subset docs/design/AIlabel_subset_30.md --corpus corpus --out ailabel/results_claude.csv --model claude-opus-4-20250514

必要:
  pip install anthropic

引数:
  --subset   : サブセットリスト（AIlabel_subset_30.md）のパス
  --corpus   : コーパスルートディレクトリ
  --out      : 出力CSVパス
  --model    : 使用モデル（デフォルト: claude-sonnet-4-20250514）
  --api-key  : APIキー（省略時はANTHROPIC_API_KEY環境変数を使用）
"""

import argparse
import csv
import json
import os
import re
import sys
import time

try:
    import anthropic
except ImportError:
    print("ERROR: anthropic パッケージが必要です")
    print("  pip install anthropic")
    sys.exit(1)

# =====================
# プロンプトテンプレート
# =====================

PROMPT_TEMPLATE = """あなたは認知的操作リスクのアノテーターです。
以下のアノテーション基準（annotation_criteria v0.6）に従い、
テキストにHIGH・MEDIUM・LOW・Intent-Unresolvedのいずれかのラベルを付けてください。

【判定基準の要約】
HIGH: H-1〜H-4のいずれか1つ以上を満たす
  H-1: 一人称体験談＋操作主体の不可視化＋外部誘導
  H-2: 並列累積エピソード＋規範収束＋反論余地の構造的不在
  H-3: 欲求喚起語彙（明示的）＋行動誘導の結合
  H-4: 恐怖・損失回避語彙＋即時外部行動誘導（2条件同時）

MEDIUM: H-1〜H-4を満たさず、M-1〜M-4のいずれかを満たす
  M-1: 間接的・漸進的行動誘導
  M-2: 検証不能な権威・統計の引用
  M-3: 商業的誘導意図（語彙密度低）
  M-4: 感情誘導語彙の近傍集中（同一段落3語以上）

LOW: HIGH・MEDIUMに該当しないと積極的に判断できる

Intent-Unresolved: 判定不能（保留）

【重要な注意事項】
- テキスト内の言語構造のみに基づいて判定する
- 発信者の属性・利益構造等テキスト外情報は使用しない
- CMIスコアは参考値。スコアに引きずられないこと
- 判定が定まらない場合はIntent-Unresolvedを使用する

【出力形式】
以下のJSON形式のみで回答してください。説明文・前置き・コードブロックは不要です。
{{
  "label": "HIGH/MEDIUM/LOW/Intent-Unresolved",
  "primary_condition": "H-1/H-2/H-3/H-4/M-1/M-2/M-3/M-4/L-1/L-2/L-3/IU",
  "confidence": "high/medium/low",
  "reason": "判定根拠を1〜2文で"
}}

【対象テキスト】
{text}
"""

VALID_LABELS = {"HIGH", "MEDIUM", "LOW", "Intent-Unresolved"}
DEFAULT_MODEL = "claude-sonnet-4-20250514"


def load_subset(subset_path):
    """AIlabel_subset_30.mdからtargetリストを読み込む"""
    targets = []
    with open(subset_path, encoding="utf-8") as f:
        for line in f:
            # | target | ... | パターンの行を抽出
            m = re.match(r"\|\s*([^|]+?)\s*\|\s*([\d.]+)\s*\|\s*(\w+)\s*\|\s*(\w[\w-]*)\s*\|", line)
            if m and m.group(1) != "target":
                targets.append({
                    "target": m.group(1).strip(),
                    "cmi": m.group(2).strip(),
                    "r8_level": m.group(3).strip(),
                    "human_label": m.group(4).strip(),
                })
    return targets


def find_text_file(target, corpus_root):
    """targetからテキストファイルのパスを解決する"""
    # フルパス形式（corpus\...）
    if os.sep in target or "/" in target:
        # corpus\ を除去してcorpus_rootと結合
        rel = target.replace("corpus\\", "").replace("corpus/", "")
        path = os.path.join(corpus_root, rel)
        if os.path.exists(path):
            return path

    # ファイル名のみの形式（note087等）
    for root, dirs, files in os.walk(corpus_root):
        for f in files:
            name = os.path.splitext(f)[0]
            if name.lower() == target.lower().replace("_", ""):
                return os.path.join(root, f)
            if f.lower() == target.lower() + ".txt":
                return os.path.join(root, f)

    return None


def annotate(client, model, text):
    """Claude APIでアノテーション実施"""
    prompt = PROMPT_TEMPLATE.format(text=text[:8000])  # 長文は8000字で切る
    message = client.messages.create(
        model=model,
        max_tokens=512,
        messages=[{"role": "user", "content": prompt}]
    )
    raw = message.content[0].text.strip()

    # JSON パース
    try:
        # コードブロック除去
        raw_clean = re.sub(r"```json|```", "", raw).strip()
        result = json.loads(raw_clean)
    except json.JSONDecodeError:
        result = {
            "label": "PARSE_ERROR",
            "primary_condition": "",
            "confidence": "",
            "reason": raw[:200]
        }

    # ラベル検証
    if result.get("label") not in VALID_LABELS:
        result["label"] = "PARSE_ERROR"

    return result


def main():
    parser = argparse.ArgumentParser(description="AIlabel annotator using Claude API")
    parser.add_argument("--subset", required=True, help="AIlabel_subset_30.md のパス")
    parser.add_argument("--corpus", required=True, help="コーパスルートディレクトリ")
    parser.add_argument("--out", required=True, help="出力CSVパス")
    parser.add_argument("--model", default=DEFAULT_MODEL, help=f"使用モデル（デフォルト: {DEFAULT_MODEL}）")
    parser.add_argument("--api-key", default=None, help="APIキー（省略時はANTHROPIC_API_KEY環境変数）")
    args = parser.parse_args()

    # APIクライアント初期化
    api_key = args.api_key or os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("ERROR: APIキーが必要です")
        print("  --api-key オプションか ANTHROPIC_API_KEY 環境変数を設定してください")
        sys.exit(1)

    client = anthropic.Anthropic(api_key=api_key)

    # サブセット読み込み
    targets = load_subset(args.subset)
    if not targets:
        print(f"ERROR: サブセットリストが読み込めませんでした: {args.subset}")
        sys.exit(1)

    print(f"モデル  : {args.model}")
    print(f"対象件数: {len(targets)}件")
    print(f"出力先  : {args.out}")
    print()

    # 出力CSVを準備
    os.makedirs(os.path.dirname(args.out) if os.path.dirname(args.out) else ".", exist_ok=True)
    fieldnames = ["target", "model", "human_label", "cmi", "r8_level",
                  "ai_label", "primary_condition", "confidence", "reason", "text_found"]

    results = []
    errors = []

    for i, item in enumerate(targets, 1):
        target = item["target"]
        print(f"[{i:02d}/{len(targets)}] {target} ... ", end="", flush=True)

        # テキストファイル解決
        text_path = find_text_file(target, args.corpus)
        if not text_path:
            print("FILE NOT FOUND")
            errors.append(target)
            results.append({
                "target": target, "model": args.model,
                "human_label": item["human_label"], "cmi": item["cmi"],
                "r8_level": item["r8_level"], "ai_label": "FILE_NOT_FOUND",
                "primary_condition": "", "confidence": "", "reason": "", "text_found": "0"
            })
            continue

        # テキスト読み込み
        try:
            with open(text_path, encoding="utf-8", errors="ignore") as f:
                text = f.read()
        except Exception as e:
            print(f"READ ERROR: {e}")
            errors.append(target)
            continue

        # API呼び出し
        try:
            result = annotate(client, args.model, text)
            print(f"{result['label']} ({result['confidence']})")
            results.append({
                "target": target, "model": args.model,
                "human_label": item["human_label"], "cmi": item["cmi"],
                "r8_level": item["r8_level"],
                "ai_label": result["label"],
                "primary_condition": result.get("primary_condition", ""),
                "confidence": result.get("confidence", ""),
                "reason": result.get("reason", ""),
                "text_found": "1"
            })
        except Exception as e:
            print(f"API ERROR: {e}")
            errors.append(target)

        # レート制限対策
        time.sleep(1.0)

    # CSV書き出し
    with open(args.out, "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)

    print()
    print(f"完了: {len(results)}件出力 / {len(errors)}件エラー")
    print(f"出力: {args.out}")

    if errors:
        print(f"\nエラー対象:")
        for e in errors:
            print(f"  {e}")

    print(f"\n次のステップ — kappa計算:")
    print(f"  python ailabel/ailabel_analyze.py --results {args.out}")


if __name__ == "__main__":
    main()
