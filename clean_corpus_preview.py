"""
clean_corpus_preview.py  v3
処理A（確実除去）のみ。ブロック判定による除去は行わない。
情報損失ゼロを最優先。
"""

import os, re
from pathlib import Path

ARCHIVE_DIR = r"D:\r8_strategy\corpus\corpus_archive"

SAMPLES = [
    ("AD_001_20260326.txt",  "投資系ブログ（PR多い・表あり）"),
    ("AD_019_20260326.txt",  "サロン系（ナビゲーション残存）"),
    ("note111.txt",          "note系（短行多い）"),
    ("SN_003_20260326.txt",  "SNS系（超短文・絵文字）"),
    ("web101.txt",           "自己啓発web（長文）"),
]

# ────────────────────────────────────────────
# 確実除去パターン（A）
# 条件：どのコーパスでも「本文である可能性がゼロ」のもののみ
# ────────────────────────────────────────────
DEFINITE_REMOVE = [
    # メタヘッダー
    re.compile(r'^\[(SOURCE|DATE|CATEGORY|TEXT)\]'),
    # URL単独行
    re.compile(r'^\s*https?://\S+\s*$'),
    # PR・広告行
    re.compile(r'^#PR[\s　]'),
    re.compile(r'^\[ad#'),
    # ハッシュタグのみ行（2個以上）
    re.compile(r'^(#\S+[\s　]*){2,}$'),
    # 画像プレースホルダ
    re.compile(r'^画像\d*$'),
    # webサイト定番ヘッダー（完全一致・疑義なし）
    re.compile(r'^コンテンツへスキップ$'),
    re.compile(r'^メニューへスキップ$'),
    re.compile(r'^ナビゲーションへスキップ$'),
    re.compile(r'^Proudly powered by'),
    re.compile(r'^Copyright\s'),
    re.compile(r'^© \d{4}'),
    re.compile(r'^All Rights Reserved'),
    # note系UI（完全一致・疑義なし）
    re.compile(r'^桜のイラスト$'),
    re.compile(r'^見出し画像$'),
    re.compile(r'^チップで応援する$'),
    re.compile(r'^いいなと思ったら応援しよう'),
    re.compile(r'^よかったらシェアしてね'),
    re.compile(r'^この記事が気に入ったら'),
    re.compile(r'^noteプレミアム$'),
    re.compile(r'^note pro$'),
    re.compile(r'^キーワードやクリエイターで検索$'),
    re.compile(r'^クリエイターへのお問い合わせ$'),
    re.compile(r'^通常ポイント利用特約$'),
    re.compile(r'^加盟店規約$'),
    re.compile(r'^資金決済法に基づく表示$'),
    re.compile(r'^特商法表記$'),
    re.compile(r'^投資情報の免責事項$'),
    # Facebook系UI
    re.compile(r'^\s*·\s*$'),
]

def is_definite_remove(line):
    s = line.strip()
    if not s:
        return False  # 空行は後で処理
    for pat in DEFINITE_REMOVE:
        if pat.search(s):
            return True
    return False

def detect_repeating_short(lines, max_len=15, min_count=2):
    """max_len文字以下の行がmin_count回以上出現するものを除去対象に"""
    from collections import Counter
    short = [l.strip() for l in lines if 1 <= len(l.strip()) <= max_len]
    counts = Counter(short)
    return {line for line, cnt in counts.items() if cnt >= min_count}

# ────────────────────────────────────────────
# 整形処理（段落・空白のみ）
# ────────────────────────────────────────────
def normalize_whitespace(text):
    # 行末空白除去
    lines = [l.rstrip() for l in text.splitlines()]
    text = "\n".join(lines)
    # 3連続以上改行 → 2改行
    text = re.sub(r'\n{3,}', '\n\n', text)
    # 先頭・末尾空白
    return text.strip()

# ────────────────────────────────────────────
# メイン整形
# ────────────────────────────────────────────
def clean(raw_text):
    lines = raw_text.splitlines()

    # 繰り返し短行を検出
    repeat_set = detect_repeating_short(lines)

    removed_lines = []
    kept_lines    = []

    for line in lines:
        s = line.strip()
        if not s:
            kept_lines.append(line)
            continue
        if is_definite_remove(line):
            removed_lines.append(("pattern", s))
            continue
        if s in repeat_set:
            removed_lines.append(("repeat", s))
            continue
        kept_lines.append(line)

    cleaned = normalize_whitespace("\n".join(kept_lines))
    return cleaned, removed_lines

# ────────────────────────────────────────────
# プレビュー出力
# ────────────────────────────────────────────
def preview_file(filepath, desc):
    with open(filepath, encoding="utf-8", errors="ignore") as f:
        raw = f.read()

    cleaned, removed = clean(raw)

    raw_len = len(raw)
    cln_len = len(cleaned)
    ratio   = (1 - cln_len / max(raw_len, 1)) * 100

    print(f"\n{'='*70}")
    print(f"【{desc}】{os.path.basename(filepath)}")
    print(f"{'='*70}")
    print(f"整形前: {raw_len:,}文字 → 整形後: {cln_len:,}文字 (-{ratio:.0f}%)")
    print(f"除去行数: {len(removed)}行")

    # 除去行一覧
    if removed:
        print(f"\n--- 除去された行（全件）---")
        for kind, line in removed:
            tag = "[パターン]" if kind == "pattern" else "[繰り返し]"
            print(f"  {tag} 「{line[:65]}」")

    # 整形後テキスト先頭500文字
    print(f"\n--- 整形後テキスト（先頭500文字）---")
    print(cleaned[:500])
    print(f"---")

    # 末尾100文字も確認（フッターが残っていないか）
    if len(cleaned) > 500:
        print(f"\n--- 整形後テキスト（末尾200文字）---")
        print(cleaned[-200:])
        print(f"---")

# ────────────────────────────────────────────
if __name__ == "__main__":
    print("=== clean_corpus サンプル確認 v3（処理Aのみ）===")
    for fname, desc in SAMPLES:
        fpath = os.path.join(ARCHIVE_DIR, fname)
        if os.path.exists(fpath):
            preview_file(fpath, desc)
        else:
            print(f"\n⚠ ファイル未発見: {fname}")
    print(f"\n{'='*70}")
    print("確認完了。除去行に本文が含まれていないか確認してください。")
