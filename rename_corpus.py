#!/usr/bin/env python3
"""
rename_corpus.py — コーパスファイル連番リネームツール

使い方:
  python rename_corpus.py note          # inbox内の全ファイルをnote_XXX.txtにリネーム
  python rename_corpus.py web           # inbox内の全ファイルをweb_XXX.txtにリネーム
  python rename_corpus.py sn            # sn_XXX.txt
  python rename_corpus.py ad            # ad_XXX.txt
  python rename_corpus.py bl            # bl_XXX.txt

手順:
  1. corpus/phase2/inbox/ にtxtファイルを入れる
  2. python rename_corpus.py <種別> を実行
  3. 自動で次の連番が振られ corpus/phase2/scan/ に移動される
"""

import os
import sys
import re
import shutil

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INBOX = os.path.join(BASE_DIR, "corpus", "phase2", "inbox")
SCAN  = os.path.join(BASE_DIR, "corpus", "phase2", "scan")

# 既存の全フォルダから最大連番を検索
PHASE2 = os.path.join(BASE_DIR, "corpus", "phase2")

VALID_TYPES = ["web", "note", "sn", "ad", "bl", "phish"]

def find_max_number():
    """phase2以下の全ファイルから最大連番を取得"""
    max_num = 0
    pattern = re.compile(r'(?:web|note|sn|ad|bl|phish|WEB|NOTE|SN|AD|BL|PHISH)[_]?(\d+)', re.IGNORECASE)
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
        print("使い方: python rename_corpus.py <種別>")
        print(f"種別: {', '.join(VALID_TYPES)}")
        sys.exit(1)

    file_type = sys.argv[1].lower()
    if file_type not in VALID_TYPES:
        print(f"エラー: 種別は {', '.join(VALID_TYPES)} のいずれか")
        sys.exit(1)

    # フォルダ作成
    os.makedirs(INBOX, exist_ok=True)
    os.makedirs(SCAN, exist_ok=True)

    # inbox内のtxtファイル取得
    txt_files = sorted([f for f in os.listdir(INBOX) if f.endswith('.txt')])
    if not txt_files:
        print(f"inbox にtxtファイルがありません: {INBOX}")
        sys.exit(0)

    # 最大連番取得
    next_num = find_max_number() + 1

    print(f"種別: {file_type}")
    print(f"開始番号: {next_num}")
    print(f"対象: {len(txt_files)} ファイル")
    print()

    for f in txt_files:
        new_name = f"{file_type}{next_num}.txt"
        src = os.path.join(INBOX, f)
        dst = os.path.join(SCAN, new_name)
        shutil.move(src, dst)
        print(f"  {f} -> {new_name}")
        next_num += 1

    print(f"\n完了: {len(txt_files)} ファイルを scan/ に移動")

if __name__ == "__main__":
    main()
