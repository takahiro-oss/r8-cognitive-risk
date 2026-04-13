#!/usr/bin/env python3
"""
url_batch.py — URL一括取得・自動リネームツール

使い方:
  python url_batch.py web    # corpus/phase2/urlfile/urls_web.txt を処理
  python url_batch.py note   # corpus/phase2/urlfile/urls_note.txt を処理
  python url_batch.py sn     # corpus/phase2/urlfile/urls_sn.txt を処理
  python url_batch.py ad     # corpus/phase2/urlfile/urls_ad.txt を処理

手順:
  1. corpus/phase2/urlfile/urls_<種別>.txt に1行1URLを記載
  2. python url_batch.py <種別> を実行
  3. 自動でテキスト取得 → inbox保存 → scan/にリネームして移動

urlファイルの書き方:
  https://example.com
  https://example2.com
  # #で始まる行はスキップ
  # 処理済みのURLはそのままにしておいてOK（再実行時は手動で削除か#コメントアウト）
"""

import requests
from bs4 import BeautifulSoup
import sys
import os
import re
import shutil

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
URLFILE_DIR = os.path.join(BASE_DIR, "corpus", "phase2", "urlfile")
INBOX       = os.path.join(BASE_DIR, "corpus", "phase2", "inbox")
SCAN        = os.path.join(BASE_DIR, "corpus", "phase2", "scan")
PHASE2      = os.path.join(BASE_DIR, "corpus", "phase2")

VALID_TYPES = ["web", "note", "sn", "ad", "bl", "phish"]


def fetch_url(url):
    """URLからテキストを取得してクリーニング"""
    headers = {"User-Agent": "Mozilla/5.0"}
    res = requests.get(url, timeout=15, headers=headers)
    res.encoding = res.apparent_encoding
    soup = BeautifulSoup(res.text, "html.parser")
    for tag in soup(["script", "style", "nav", "header", "footer", "aside"]):
        tag.decompose()
    lines = [l.strip() for l in soup.get_text(separator="\n").splitlines() if l.strip()]
    return "\n".join(lines)


def find_max_number():
    """phase2以下の全ファイルから最大連番を取得"""
    max_num = 0
    pattern = re.compile(r'(?:web|note|sn|ad|bl|phish)[_]?(\d+)', re.IGNORECASE)
    for root, dirs, files in os.walk(PHASE2):
        for f in files:
            m = pattern.search(f)
            if m:
                num = int(m.group(1))
                if num > max_num:
                    max_num = num
    return max_num


def main():
    if len(sys.argv) < 2:
        print("使い方: python url_batch.py <種別>")
        print(f"種別: {', '.join(VALID_TYPES)}")
        sys.exit(1)

    file_type = sys.argv[1].lower()
    if file_type not in VALID_TYPES:
        print(f"エラー: 種別は {', '.join(VALID_TYPES)} のいずれか")
        sys.exit(1)

    urlfile = os.path.join(URLFILE_DIR, f"urls_{file_type}.txt")
    if not os.path.exists(urlfile):
        os.makedirs(URLFILE_DIR, exist_ok=True)
        # テンプレートファイルを作成
        with open(urlfile, "w", encoding="utf-8") as f:
            f.write(f"# urls_{file_type}.txt\n")
            f.write("# 1行1URL。#で始まる行はスキップ\n")
            f.write("# 例: https://example.com\n")
        print(f"[作成] URLファイルを作成しました: {urlfile}")
        print("URLを記入してから再実行してください。")
        sys.exit(0)

    os.makedirs(INBOX, exist_ok=True)
    os.makedirs(SCAN, exist_ok=True)

    # URLリスト読み込み
    with open(urlfile, encoding="utf-8") as f:
        urls = [l.strip() for l in f if l.strip() and not l.strip().startswith("#")]

    if not urls:
        print(f"処理対象のURLがありません: {urlfile}")
        sys.exit(0)

    print(f"種別: {file_type}")
    print(f"対象URL: {len(urls)} 件")
    print()

    # 取得・inbox保存
    saved = []
    for url in urls:
        try:
            text = fetch_url(url)
            # inboxに一時ファイル名で保存
            tmp_name = re.sub(r"[\\/:*?\"<>|]", "_", url.replace("https://","").replace("http://",""))[:60] + ".txt"
            tmp_path = os.path.join(INBOX, tmp_name)
            with open(tmp_path, "w", encoding="utf-8") as f:
                f.write(url + "\n\n")
                f.write(text)
            print(f"[OK] {url}")
            saved.append(tmp_path)
        except Exception as e:
            print(f"[ERROR] {url} → {e}")

    if not saved:
        print("\n取得成功ファイルなし。終了します。")
        sys.exit(0)

    # リネーム・scan移動
    next_num = find_max_number() + 1
    print(f"\n--- リネーム開始（{file_type}{next_num}〜） ---")

    inbox_files = sorted([f for f in os.listdir(INBOX) if f.endswith(".txt")])
    renamed = []
    for f in inbox_files:
        new_name = f"{file_type}{next_num}.txt"
        src = os.path.join(INBOX, f)
        dst = os.path.join(SCAN, new_name)
        shutil.move(src, dst)
        print(f"  {f[:40]}... -> {new_name}" if len(f) > 40 else f"  {f} -> {new_name}")
        renamed.append(dst)
        next_num += 1

    print(f"\n完了: {len(renamed)} ファイルを scan/ に保存")
    print("\n次のステップ — スキャン:")
    targets = " ".join(renamed)
    print(f"  python mass_audit.py --targets {' '.join(renamed[:3])}{'...' if len(renamed) > 3 else ''}")
    print(f"  --out data/results/scan_batch.csv --append")


if __name__ == "__main__":
    main()
