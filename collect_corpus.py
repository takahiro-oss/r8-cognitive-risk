"""
collect_corpus.py
-----------------
R8 Phase2 コーパス収集スクリプト
役割：URLリストを読み込み、テキストを取得してcorpus/phase2/に保存する

使い方：
1. urls.txt にURLを追記する（フォーマットは下記参照）
2. python collect_corpus.py を実行する

urls.txtのフォーマット：
    # --- [AD] 投資詐欺系 ---
    https://example.com/
    # --- [BL] 自己啓発系 ---
    https://example2.com/

カテゴリ略称：
    AD = 商業広告・マーケティング
    SN = SNSテキスト
    WEB = Webサイト
    BL = ブログ
    NT = 中立テキスト（対照群）
    PO = 政治的テキスト
"""

import os
import re
import requests
from bs4 import BeautifulSoup
from datetime import datetime

# ===========================
# 設定
# ===========================
BASE_DIR = r'D:\r8_strategy'
INPUT_FILE = os.path.join(BASE_DIR, 'urls.txt')
SAVE_DIR = os.path.join(BASE_DIR, 'corpus', 'phase2')
LOG_FILE = os.path.join(BASE_DIR, 'fetch_log.txt')
TARGETS_FILE = os.path.join(SAVE_DIR, 'targets.txt')
def get_next_index(save_dir):
    import glob, re
    files = glob.glob(os.path.join(save_dir, '*.txt'))
    indices = []
    for f in files:
        match = re.search(r'_(\d{3})_', os.path.basename(f))
        if match:
            indices.append(int(match.group(1)))
    return max(indices) + 1 if indices else 34

TODAY_STR = datetime.now().strftime("%Y%m%d")

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    )
}

# ===========================
# メイン処理
# ===========================
def collect():
    os.makedirs(SAVE_DIR, exist_ok=True)

    if not os.path.exists(INPUT_FILE):
        print(f"[Error] {INPUT_FILE} が見つかりません。")
        print("urls.txt を作成してURLを記入してください。")
        return

    with open(INPUT_FILE, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    current_category = "ETC"
    current_idx = get_next_index(SAVE_DIR)
    saved_files = []

    for line in lines:
        line = line.strip()
        if not line:
            continue

        # カテゴリ行の処理
        if line.startswith('#'):
            match = re.search(r'\[([A-Z]+)\]', line)
            if match:
                current_category = match.group(1)
            continue

        # URL取得・保存
        url = line
        file_name = f"{current_category}_{current_idx:03}_{TODAY_STR}.txt"
        save_path = os.path.join(SAVE_DIR, file_name)

        print(f"Fetching [{current_idx:03}] {url} ... ", end="", flush=True)

        try:
            response = requests.get(url, headers=HEADERS, timeout=15)
            response.raise_for_status()
            response.encoding = response.apparent_encoding

            soup = BeautifulSoup(response.text, 'html.parser')
            for tag in soup(["script", "style", "nav", "footer", "header"]):
                tag.decompose()

            text = soup.get_text(separator="\n", strip=True)

            if len(text) < 100:
                raise ValueError("テキストが短すぎます（JSレンダリングの可能性）")

            with open(save_path, 'w', encoding='utf-8') as f_out:
                f_out.write(f"[SOURCE] {url}\n")
                f_out.write(f"[DATE] {TODAY_STR}\n")
                f_out.write(f"[CATEGORY] {current_category}\n")
                f_out.write("[TEXT]\n")
                f_out.write(text)

            print(f"OK -> {file_name}")
            saved_files.append(f"corpus/phase2/{file_name}")
            current_idx += 1

        except Exception as e:
            msg = f"FAILED [{current_idx:03}] {url} -> {e}"
            print(f"FAILED ({e})")
            with open(LOG_FILE, 'a', encoding='utf-8') as f_log:
                f_log.write(f"{datetime.now()} {msg}\n")

    # targets.txtに追記
    if saved_files:
        with open(TARGETS_FILE, 'a', encoding='utf-8') as f_targets:
            for path in saved_files:
                f_targets.write(path + "\n")
        print(f"\n{len(saved_files)}件を保存しました。")
        print(f"targets.txt に追記しました。")
        print(f"\n次のコマンドでスキャンしてください：")
        print(f"python mass_audit.py corpus/phase2/targets.txt --out data/results/phase2_{TODAY_STR}.csv")
    else:
        print("\n保存されたファイルがありません。fetch_log.txtを確認してください。")

if __name__ == "__main__":
    collect()
