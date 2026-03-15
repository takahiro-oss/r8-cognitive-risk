#!/usr/bin/env python3
# add_sample.py — R8 検証データ追加ツール v2
# 使い方: python add_sample.py [URL or ファイルパス]

import sys
import os
import csv
import re

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from r8 import THRESHOLDS, WEIGHTS, CATEGORY_LABELS, cmi_level, analyze
except ImportError:
    print("[Error] r8.py が見つかりません。")
    sys.exit(1)

if sys.stdout.encoding and sys.stdout.encoding.lower() in ("cp932", "shift_jis", "shift-jis", "mbcs"):
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

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

BASE_DIR    = os.path.dirname(os.path.abspath(__file__))
TARGETS_CSV = os.path.join(BASE_DIR, "data", "targets", "targets.csv")
HEADERS     = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}

def get_text(target):
    if target.startswith("http://") or target.startswith("https://"):
        if not WEB_AVAILABLE:
            return None, "[Error] requests/BeautifulSoup がありません"
        try:
            resp = requests.get(target, headers=HEADERS, timeout=15)
            resp.encoding = resp.apparent_encoding
            soup = BeautifulSoup(resp.text, "html.parser")
            for tag in soup(["script", "style", "nav", "footer", "header", "aside"]):
                tag.decompose()
            text = soup.get_text(separator="\n", strip=True)
            text = re.sub(r"\n{3,}", "\n\n", text)
            return text, None
        except Exception as e:
            return None, f"[Error] {e}"
    if target.lower().endswith(".pdf"):
        if not PDF_ENGINE:
            return None, "[Error] PyMuPDF がありません"
        try:
            doc = fitz.open(target)
            return "\n".join(page.get_text() for page in doc), None
        except Exception as e:
            return None, f"[Error] {e}"
    try:
        with open(target, "r", encoding="utf-8", errors="ignore") as f:
            return f.read(), None
    except FileNotFoundError:
        return None, f"[Error] ファイル未検出: {target}"

def compute_cmi(text):
    raw = analyze(text)
    ri  = {cat: min(raw.get(cat, 0) / THRESHOLDS[cat], 1.0) for cat in WEIGHTS}
    cmi = round(sum(WEIGHTS[c] * ri[c] * 100 for c in WEIGHTS), 1)
    return cmi, ri

def append_to_targets(target, label, cmi):
    os.makedirs(os.path.dirname(TARGETS_CSV), exist_ok=True)
    existing = set()
    if os.path.isfile(TARGETS_CSV):
        with open(TARGETS_CSV, "r", encoding="utf-8-sig", errors="ignore") as f:
            for row in csv.DictReader(f):
                existing.add(row.get("source", "").strip())
    if target in existing:
        print(f"\n  [SKIP] 既に登録済みです")
        return False
    needs_header = not os.path.isfile(TARGETS_CSV) or os.path.getsize(TARGETS_CSV) == 0
    with open(TARGETS_CSV, "a", newline="", encoding="utf-8-sig") as f:
        writer = csv.writer(f)
        if needs_header:
            writer.writerow(["source", "label", "note"])
        writer.writerow([target, label, f"CMI{cmi:.1f}・自動追記"])
    return True

def print_stats():
    if not os.path.isfile(TARGETS_CSV):
        return
    rows = []
    with open(TARGETS_CSV, "r", encoding="utf-8-sig", errors="ignore") as f:
        for row in csv.DictReader(f):
            rows.append(row)
    if not rows:
        return
    total  = len(rows)
    high   = len([r for r in rows if r.get("label","").upper() == "HIGH"])
    medium = len([r for r in rows if r.get("label","").upper() == "MEDIUM"])
    low    = len([r for r in rows if r.get("label","").upper() == "LOW"])
    cmis   = [float(m.group(1)) for r in rows for m in [re.search(r"CMI(\d+\.?\d*)", r.get("note",""))] if m]
    print("\n" + "=" * 50)
    print("  corpus統計")
    print("=" * 50)
    print(f"  総数: {total}件  進捗: {total/60*100:.0f}%  (目標60件)")
    print(f"  HIGH:   {high:2d}件  {'✅' if high>=20 else f'あと{20-high}件必要'}")
    print(f"  MEDIUM: {medium:2d}件  {'✅' if medium>=20 else f'あと{20-medium}件必要'}")
    print(f"  LOW:    {low:2d}件  {'✅' if low>=20 else f'あと{20-low}件必要'}")
    if cmis:
        print(f"  平均CMI: {sum(cmis)/len(cmis):.1f}  最大: {max(cmis):.1f}  最小: {min(cmis):.1f}")
    print("=" * 50 + "\n")

def main():
    if len(sys.argv) < 2:
        print("使い方: python add_sample.py [URL or ファイルパス]")
        print("例:     python add_sample.py https://example.com/lp/")
        sys.exit(1)

    target = sys.argv[1].strip()
    print(f"\n[add_sample] {target[:70]}")
    print("-" * 50)

    text, error = get_text(target)
    if error:
        print(f"[FAILED] {error}")
        print("  → JS動的サイトの可能性: ブラウザでテキストをコピー→txtに保存→再実行")
        sys.exit(1)
    if not text or len(text.strip()) < 50:
        print("[FAILED] テキストが短すぎます")
        sys.exit(1)

    cmi, ri = compute_cmi(text)
    label   = cmi_level(cmi).split()[0]

    print(f"  CMI  : {cmi:5.1f} / 100  [{label}]")
    flagged = sorted([(c,v) for c,v in ri.items() if v >= 0.5], key=lambda x: x[1], reverse=True)[:3]
    for cat, v in flagged:
        print(f"  Flag : {CATEGORY_LABELS[cat].split('(')[0].strip()} ({v:.2f})")

    added = append_to_targets(target, label, cmi)
    if added:
        print(f"\n  [OK] targets.csv に追記: {label} (CMI {cmi:.1f})")

    print_stats()

if __name__ == "__main__":
    main()
