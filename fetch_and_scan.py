import sys, os, re, requests
from bs4 import BeautifulSoup
from datetime import datetime

BASE_DIR    = "D:/r8_strategy"
TODO_FILE   = f"{BASE_DIR}/urls_todo.txt"
CORPUS_DIR  = f"{BASE_DIR}/corpus/phase2"
RESULTS_DIR = f"{BASE_DIR}/data/results"
MASS_SCRIPT = f"{BASE_DIR}/mass_audit.py"
TMP_TARGET  = f"{BASE_DIR}/tmp_target.txt"

def normalize_text(text):
    text = text.replace('\u3000', ' ')
    text = re.sub(r'[ \t]+', ' ', text)
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip()

def fetch_url(url):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    try:
        r = requests.get(url, headers=headers, timeout=15)
        r.encoding = r.apparent_encoding
        if r.status_code != 200:
            return None, f"HTTP {r.status_code}"
        soup = BeautifulSoup(r.text, 'html.parser')
        for tag in soup(['script', 'style', 'nav', 'footer', 'header', 'aside']):
            tag.decompose()
        text = soup.get_text(separator='\n')
        text = normalize_text(text)
        if len(text) < 200:
            return None, "テキスト短すぎ"
        return text, None
    except Exception as e:
        return None, str(e)

def load_todo(todo_file):
    if not os.path.exists(todo_file):
        print(f"[ERROR] {todo_file} が見つかりません")
        sys.exit(1)
    entries = []
    with open(todo_file, 'r', encoding='utf-8') as f:
        for i, line in enumerate(f, 1):
            line = line.rstrip('\n')
            if not line or line.startswith('#') or line.startswith('[済]'):
                continue
            parts = line.split('\t')
            if len(parts) < 2:
                continue
            entries.append((i, parts[0].strip(), parts[1].strip(), line))
    return entries

def mark_done(todo_file, line_num, original_line):
    with open(todo_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    if lines[line_num - 1].rstrip('\n') == original_line:
        lines[line_num - 1] = f"[済] {original_line}\n"
        with open(todo_file, 'w', encoding='utf-8') as f:
            f.writelines(lines)

def main():
    today = datetime.now().strftime('%Y%m%d')
    csv_out = f"{RESULTS_DIR}/phase2_{today}.csv"

    print("=" * 50)
    print("  R8 バッチ収集・スキャン")
    print(f"  出力CSV: phase2_{today}.csv")
    print("=" * 50)

    entries = load_todo(TODO_FILE)
    if not entries:
        print("未処理のURLがありません。")
        sys.exit(0)

    print(f"未処理URL: {len(entries)}件\n")
    success = 0
    failed = 0

    for line_num, url, file_id, original_line in entries:
        print(f"[{success + failed + 1}/{len(entries)}] {file_id}")
        print(f"  URL: {url}")

        text, error = fetch_url(url)
        if error:
            print(f"  → 失敗: {error}\n")
            failed += 1
            continue

        out_path = f"{CORPUS_DIR}/{file_id}.txt"
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(text)
        print(f"  → 保存: {out_path}（{len(text)}文字）")

        # 一括CSVに追記（appendモード）
        with open(TMP_TARGET, 'w', encoding='utf-8') as f:
            f.write(out_path + '\n')
        append_flag = "--append" if os.path.exists(csv_out) else ""
        os.system(f'python {MASS_SCRIPT} {TMP_TARGET} --out {csv_out} {append_flag}')

        mark_done(TODO_FILE, line_num, original_line)
        print(f"  → 完了\n")
        success += 1

    print("=" * 50)
    print(f"  完了: {success}件 / 失敗: {failed}件")
    print(f"  CSV: {csv_out}")
    print("=" * 50)

if __name__ == "__main__":
    main()
