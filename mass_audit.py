#!/usr/bin/env python3
# mass_audit.py — R8 Batch Auditor v4
# CMI (Cognitive Manipulation Index) 対応版
# v2の機能 + Gemini版の良点（追記モード・timestamp・run_audit分離）を統合

import sys
import io
import re
import os
import csv
from datetime import datetime

# Windows cp932環境でのUnicodeEncodeError対策
if sys.stdout.encoding and sys.stdout.encoding.lower() in ("cp932", "shift_jis", "shift-jis", "mbcs"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

# --- r8.py を同一ディレクトリからインポート ---
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
try:
    import r8
    from r8 import THRESHOLDS, WEIGHTS, CATEGORY_LABELS, cmi_level
except ImportError:
    print("[Error] r8.py が見つかりません。同一ディレクトリに配置してください。")
    sys.exit(1)

# --- 外部ライブラリ ---
try:
    import requests
    from bs4 import BeautifulSoup
    WEB_AVAILABLE = True
except ImportError:
    WEB_AVAILABLE = False

try:
    import fitz
    PDF_ENGINE = "pymupdf"
except ImportError:
    PDF_ENGINE = None

# ===========================
# テキスト取得
# ===========================
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    )
}

def fetch_url(url):
    if not WEB_AVAILABLE:
        return None, "[Error] requests/BeautifulSoup がありません"
    try:
        resp = requests.get(url, headers=HEADERS, timeout=15)
        resp.encoding = resp.apparent_encoding
        soup = BeautifulSoup(resp.text, "html.parser")
        for tag in soup(["script", "style", "nav", "footer", "header", "aside"]):
            tag.decompose()
        text = soup.get_text(separator="\n", strip=True)
        text = re.sub(r"\n{3,}", "\n\n", text)
        return text, None
    except Exception as e:
        return None, f"[Error] URL取得失敗: {e}"

def fetch_pdf(path):
    if not PDF_ENGINE:
        return None, "[Error] PyMuPDF がありません"
    try:
        doc = fitz.open(path)
        return "\n".join(page.get_text() for page in doc), None
    except Exception as e:
        return None, f"[Error] PDF読み込み失敗: {e}"

def fetch_text(path):
    try:
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            return f.read(), None
    except FileNotFoundError:
        return None, f"[Error] ファイル未検出: {path}"

def get_text(target):
    if target.startswith("http://") or target.startswith("https://"):
        return fetch_url(target)
    if target.lower().endswith(".pdf"):
        return fetch_pdf(target)
    return fetch_text(target)

# ===========================
# 1件分析（Gemini版由来: 関数分離）
# ===========================
def run_audit(target):
    """
    1ターゲットを分析して結果辞書を返す。
    エラー時も同じ構造で返すため呼び出し側でのハンドリングが簡潔になる。
    """
    text, error = get_text(target)

    base = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "target":    target,
        "cmi":       "",
        "level":     "ERROR",
        "error":     None,
    }
    # カテゴリ列を空で初期化（エラー時もCSV行が揃う）
    for cat in CATEGORY_LABELS:
        base[cat] = ""

    if error:
        base["error"] = error
        return base
    if not text or len(text.strip()) < 50:
        base["error"] = "[Error] テキストが短すぎます（50文字未満）"
        return base

    raw = r8.analyze(text)
    ri  = {cat: min(raw.get(cat, 0) / THRESHOLDS[cat], 1.0) for cat in WEIGHTS}
    cmi = round(sum(WEIGHTS[c] * ri[c] * 100 for c in WEIGHTS), 1)

    base["cmi"]   = cmi
    base["level"] = cmi_level(cmi).split()[0]
    for cat in CATEGORY_LABELS:
        base[cat] = round(ri.get(cat, 0), 3)

    return base

# ===========================
# ターゲットリスト読み込み
# ===========================
def load_targets(list_file):
    """
    以下の形式に対応:
    - 1行1エントリのテキストファイル（# コメント行はスキップ）
    - CSVファイル: source列 または 1列目を使用（ヘッダー行自動スキップ）
    """
    targets = []
    is_csv  = list_file.lower().endswith(".csv")

    with open(list_file, "r", encoding="utf-8-sig", errors="ignore") as f:
        if is_csv:
            reader = csv.DictReader(f)
            for row in reader:
                val = row.get("source", list(row.values())[0] if row else "").strip()
                if val and not val.startswith("#"):
                    targets.append(val)
        else:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#"):
                    targets.append(line)
    return targets

# ===========================
# 出力フォーマット
# ===========================
def bar(v, width=16):
    filled = max(0, min(width, round(v * width)))
    return "[" + "█" * filled + "░" * (width - filled) + f"] {v:.2f}"

def print_summary(results):
    """results: list of run_audit()が返す辞書"""
    ok = [r for r in results if r["error"] is None]
    ng = [r for r in results if r["error"] is not None]
    ok_sorted = sorted(ok, key=lambda x: x["cmi"], reverse=True)

    print("\n" + "=" * 60)
    print("  R8 Mass Audit v3 — CMI Ranking (高リスク順)")
    print("=" * 60)

    for rank, res in enumerate(ok_sorted, 1):
        level = cmi_level(res["cmi"])
        label = os.path.basename(res["target"])[:42]
        print(f"\n  #{rank:02d}  CMI: {res['cmi']:5.1f}  [{level}]")
        print(f"       {label}")
        flagged = {cat: res[cat] for cat in CATEGORY_LABELS if isinstance(res[cat], float) and res[cat] >= 0.5}
        if flagged:
            top = sorted(flagged.items(), key=lambda x: x[1], reverse=True)[:4]
            for cat, v in top:
                lbl = CATEGORY_LABELS[cat].split("(")[0].strip()
                print(f"       {lbl:<30} {bar(v)}")
        else:
            print(f"       (フラグなし)")

    if ng:
        print(f"\n  --- 取得失敗: {len(ng)}件 ---")
        for r in ng:
            print(f"  {os.path.basename(r['target'])}: {r['error']}")

    print("\n" + "=" * 60)
    if ok_sorted:
        avg = sum(r["cmi"] for r in ok_sorted) / len(ok_sorted)
        hi  = sum(1 for r in ok_sorted if r["cmi"] >= 60)
        med = sum(1 for r in ok_sorted if 35 <= r["cmi"] < 60)
        lo  = sum(1 for r in ok_sorted if r["cmi"] < 35)
        print(f"  件数: {len(ok_sorted)}件  平均CMI: {avg:.1f}")
        print(f"  HIGH: {hi}件  MEDIUM: {med}件  LOW: {lo}件")
    print("=" * 60 + "\n")

def save_csv(results, output_path, append=False):
    """
    結果をCSVに保存。
    append=True の場合は追記モード（Gemini版由来）。
    ファイルが存在しない場合はヘッダーを自動付与。
    """
    file_exists = os.path.isfile(output_path)
    mode = "a" if append else "w"

    fieldnames = ["timestamp", "target", "cmi", "level", "error"] + list(CATEGORY_LABELS.keys())

    with open(output_path, mode, newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        # 新規ファイル or 上書きモードの場合はヘッダーを書く
        if not file_exists or not append:
            writer.writeheader()
        for res in results:
            writer.writerow(res)

    print(f"  [CSV] 保存完了: {output_path}")


# ===========================
# auto-label: targets.csvへの自動追記
# ===========================
def auto_label_and_append(results, targets_csv):
    """
    スキャン結果をtargets.csvに自動追記する。
    CMIからlabelを自動判定。既存エントリは上書きしない。
    """
    # 既存エントリを読み込む
    existing = set()
    if os.path.isfile(targets_csv):
        with open(targets_csv, "r", encoding="utf-8-sig", errors="ignore") as f:
            reader = csv.DictReader(f)
            for row in reader:
                existing.add(row.get("source", "").strip())

    added = 0
    with open(targets_csv, "a", newline="", encoding="utf-8-sig") as f:
        writer = csv.writer(f)
        # ヘッダーがなければ追加
        if not os.path.isfile(targets_csv) or os.path.getsize(targets_csv) == 0:
            writer.writerow(["source", "label", "note"])

        for res in results:
            if res["error"]:
                continue
            target = res["target"]
            if target in existing:
                print(f"  [SKIP] 既存エントリ: {os.path.basename(target)}")
                continue
            label = cmi_level(res["cmi"]).split()[0]
            note  = f"CMI{res['cmi']:.1f}・自動追記"
            writer.writerow([target, label, note])
            print(f"  [ADD]  {os.path.basename(target)[:40]} → {label} (CMI {res['cmi']:.1f})")
            added += 1

    print(f"\n  targets.csv に {added}件 追記しました: {targets_csv}")
    return added

# ===========================
# 統計サマリー
# ===========================
def print_corpus_stats(targets_csv):
    """
    targets.csvの現在の全サンプルを統計解析して表示する。
    """
    if not os.path.isfile(targets_csv):
        print("  [Stats] targets.csvが見つかりません")
        return

    rows = []
    with open(targets_csv, "r", encoding="utf-8-sig", errors="ignore") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)

    if not rows:
        print("  [Stats] サンプルが0件です")
        return

    total  = len(rows)
    high   = [r for r in rows if r.get("label","").upper() == "HIGH"]
    medium = [r for r in rows if r.get("label","").upper() == "MEDIUM"]
    low    = [r for r in rows if r.get("label","").upper() == "LOW"]

    # CMI値を抽出（noteに含まれる場合）
    import re
    cmis = []
    for r in rows:
        note = r.get("note", "")
        m = re.search(r"CMI(\d+\.?\d*)", note)
        if m:
            cmis.append(float(m.group(1)))

    print("\n" + "=" * 60)
    print("  corpus統計サマリー")
    print("=" * 60)
    print(f"  総サンプル数 : {total}件  (目標: 60件・進捗: {total/60*100:.0f}%)")
    print(f"  HIGH         : {len(high)}件  (目標: 20件)")
    print(f"  MEDIUM       : {len(medium)}件  (目標: 20件)")
    print(f"  LOW          : {len(low)}件  (目標: 20件)")
    if cmis:
        print(f"\n  CMI統計（記録済み{len(cmis)}件）")
        print(f"  平均CMI      : {sum(cmis)/len(cmis):.1f}")
        print(f"  最大CMI      : {max(cmis):.1f}")
        print(f"  最小CMI      : {min(cmis):.1f}")

    # 不足カテゴリの警告
    print("\n  [優先収集カテゴリ]")
    if len(high) < 20:
        print(f"  ⚠ HIGH   あと{20-len(high)}件必要")
    if len(medium) < 20:
        print(f"  ⚠ MEDIUM あと{20-len(medium)}件必要")
    if len(low) < 20:
        print(f"  ⚠ LOW    あと{20-len(low)}件必要")
    if len(high) >= 20 and len(medium) >= 20 and len(low) >= 20:
        print(f"  ✅ 全カテゴリ目標達成！")
    print("=" * 60 + "\n")

# ===========================
# バッチ実行
# ===========================
def run(targets, csv_out=None, append=False):
    results = []
    total   = len(targets)

    print(f"\n[Mass Audit] {total}件の処理を開始します...\n")

    for i, target in enumerate(targets, 1):
        label = os.path.basename(target)[:50]
        print(f"  [{i:02d}/{total:02d}] {label} ", end="", flush=True)
        res = run_audit(target)
        if res["error"]:
            print(f"-> FAILED: {res['error']}")
        else:
            level = cmi_level(res["cmi"]).split()[0]
            print(f"-> CMI: {res['cmi']:5.1f}  [{level}]")
        results.append(res)

    print_summary(results)

    if csv_out:
        save_csv(results, csv_out, append=append)

    return results

# ===========================
# エントリポイント
# ===========================
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="R8 Mass Audit v3 — バッチCMIスキャナ",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
使い方の例:
  # CSVリストから一括スキャン（CSV自動出力）
  python mass_audit.py data/targets/targets.csv

  # 出力先を指定
  python mass_audit.py data/targets/targets.csv --out data/results/result.csv

  # 既存CSVに追記
  python mass_audit.py data/targets/targets.csv --out data/results/result.csv --append

  # ターゲットを直接指定
  python mass_audit.py --targets https://example.com file.txt doc.pdf
        """
    )
    parser.add_argument("list_file", nargs="?", help="ターゲットリスト (.txt or .csv)")
    parser.add_argument("--targets", nargs="+", help="ターゲットを直接指定")
    parser.add_argument("--out",    metavar="FILE", help="出力CSVパス")
    parser.add_argument("--append",     action="store_true", help="既存CSVに追記する")
    parser.add_argument("--auto-label", action="store_true", help="CMIから自動でlabel判定しtargets.csvに追記")
    parser.add_argument("--stats",      action="store_true", help="targets.csvの統計サマリーを表示")

    args = parser.parse_args()

    targets = []
    if args.list_file:
        if not os.path.exists(args.list_file):
            print(f"[Error] ファイルが見つかりません: {args.list_file}")
            sys.exit(1)
        targets = load_targets(args.list_file)
    elif args.targets:
        targets = args.targets
    else:
        parser.print_help()
        sys.exit(1)

    if not targets:
        print("[Error] ターゲットが0件です。")
        sys.exit(1)

    csv_out = args.out
    if not csv_out:
        results_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "results")
        os.makedirs(results_dir, exist_ok=True)
        ts      = datetime.now().strftime("%Y%m%d_%H%M%S")
        csv_out = os.path.join(results_dir, f"r8_audit_{ts}.csv")

    results = run(targets, csv_out, append=args.append)

    # auto-label: targets.csvへの自動追記
    if getattr(args, 'auto_label', False):
        targets_csv = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "targets", "targets.csv")
        auto_label_and_append(results, targets_csv)

    # stats: 統計サマリー表示
    if getattr(args, 'stats', False) or getattr(args, 'auto_label', False):
        targets_csv = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "targets", "targets.csv")
        print_corpus_stats(targets_csv)
