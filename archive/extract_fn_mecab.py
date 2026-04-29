"""
extract_fn_mecab.py
MeCab形態素解析による語彙的FN辞書候補抽出

処理内容：
1. 語彙的FN48件のテキストを形態素解析
2. 名詞・動詞・形容詞・副詞の複合フレーズ（1〜4形態素）を抽出
3. Document Frequency（出現ファイル数）でカウント
4. 全コーパスとのDF比較でFPリスクを評価
5. 現行辞書語彙を除外
6. 候補をCSV出力 + ターミナルプレビュー

出力: D:\r8_strategy\data\results\fn_mecab_candidates.csv
"""

import csv
import os
import re
from collections import Counter, defaultdict
import MeCab

# ===========================
# 設定
# ===========================
CORPUS_ARCHIVE = r"D:\r8_strategy\corpus\phase2\corpus_archive"
SNAPSHOT_CSV   = r"D:\r8_strategy\data\results\corpus_snapshot.csv"
OUTPUT_CSV     = r"D:\r8_strategy\data\results\fn_mecab_candidates.csv"

# MeCab初期化
tagger = MeCab.Tagger()

# 対象品詞（これらを含むフレーズを抽出）
TARGET_POS = {
    '名詞', '動詞', '形容詞', '副詞', '感動詞', '接頭辞'
}

# 除外品詞（これだけで構成されるフレーズは不要）
SKIP_ONLY_POS = {
    '助詞', '助動詞', '記号', '補助記号', '空白', '接続詞'
}

# 現行辞書語彙（除外用）
EXISTING_DICT = {
    "急騰","大急騰","急上昇","爆上げ","今だけ","期間限定","急げ","残りわずか",
    "本日限定","締め切り","今すぐ","最後のチャンス","今が買い時","今のうち",
    "LINE登録","友達追加","限定公開","削除前に","消される前に","以内に削除",
    "絶対","必ず","完全","間違いなく","確実に","全員","誰でも","保証",
    "奇跡","衝撃","感動","驚愕","革命的","人生が変わる","人生が好転",
    "危険","崩壊","破滅","恐怖","脅威","危機","手遅れ","このままでは",
    "衝撃の事実","知らないと損","知らないと危険","の末路","99%が知らない",
    "出会い募集","即会い","恋活","割り切り","真剣な出会い",
    "ほとんどの人が知らない","期待される","可能性がある","かもしれない",
    "激減","劇的に改善","驚異の","鳥肌が立った","今すぐ登録",
    "死ぬまで働け","お金以上のもの","ありがとうを集める",
}

# ノイズフレーズ（プラットフォームUI・著者名等）
NOISE_PATTERNS = [
    r'弁護士リュウ', r'チップで応援', r'いいなと思ったら',
    r'note', r'フォロー', r'コメント', r'シェア',
    r'プロフィール', r'マガジン', r'スキ',
    r'^\d+$',  # 数字のみ
]
NOISE_RE = re.compile('|'.join(NOISE_PATTERNS))

# ===========================
# 語彙的FN対象ファイルの特定
# ===========================
def get_lexical_fn_targets():
    targets = set()
    with open(SNAPSHOT_CSV, encoding='utf-8-sig') as f:
        for row in csv.DictReader(f):
            if row.get('human_label','').strip() != 'HIGH':
                continue
            if row.get('level','').strip() == 'HIGH':
                continue
            rf = row.get('riskfactor','').strip()
            if 'False Negative' in rf:
                continue
            try:
                hype   = float(row.get('hype','0').strip() or 0)
                fear   = float(row.get('fear','0').strip() or 0)
                sexual = float(row.get('sexual_induction','0').strip() or 0)
            except:
                continue
            if 'Desire Activation' in rf and (sexual > 0 or hype > 0.3):
                targets.add(row['target'].strip())
            elif 'No academic/empirical support' in rf and (hype > 0.3 or fear > 0.5):
                targets.add(row['target'].strip())
            elif 'Emotional Induction' in rf and (fear > 0.5 or hype > 0.3):
                targets.add(row['target'].strip())
    return targets

def find_file(target, archive_dir):
    tl = target.lower().replace(' ','')
    for fname in os.listdir(archive_dir):
        if fname.lower() == 'readme.txt':
            continue
        fl = fname.lower()
        stem = os.path.splitext(fl)[0].replace('_','').replace('-','')
        tl2  = tl.replace('_','').replace('-','')
        if stem == tl2 or stem.startswith(tl2):
            return os.path.join(archive_dir, fname)
    return None

# ===========================
# MeCabによるフレーズ抽出
# ===========================
def parse_to_morphemes(text):
    """テキストを形態素列に変換"""
    # 前処理
    text = re.sub(r'https?://\S+', '', text)
    text = re.sub(r'<[^>]+>', '', text)
    text = re.sub(r'[a-zA-Z0-9]{5,}', '', text)  # 長い英数字除去

    morphemes = []
    node = tagger.parseToNode(text)
    while node:
        surface = node.surface
        feature = node.feature.split(',')
        pos = feature[0] if feature else ''
        pos2 = feature[1] if len(feature) > 1 else ''
        base = feature[7] if len(feature) > 7 else surface  # 基本形
        if surface and pos not in ('BOS/EOS',):
            morphemes.append({
                'surface': surface,
                'pos': pos,
                'pos2': pos2,
                'base': base,
            })
        node = node.next
    return morphemes

def extract_phrases(morphemes, max_len=4):
    """
    形態素列から意味のあるフレーズを抽出。
    連続する名詞・動詞・形容詞等の組み合わせを1〜max_len形態素でスライド。
    """
    phrases = set()
    n = len(morphemes)

    for i in range(n):
        for length in range(1, max_len + 1):
            if i + length > n:
                break
            window = morphemes[i:i+length]

            # 全要素が除外品詞なら skip
            pos_set = {m['pos'] for m in window}
            if pos_set.issubset(SKIP_ONLY_POS):
                continue

            # 対象品詞を1つも含まなければ skip
            if not pos_set.intersection(TARGET_POS):
                continue

            phrase = ''.join(m['surface'] for m in window).strip()

            # フィルタ
            if len(phrase) < 3:
                continue
            if phrase in EXISTING_DICT:
                continue
            if NOISE_RE.search(phrase):
                continue
            # ひらがなのみ → skip
            if re.match(r'^[\u3040-\u309f]+$', phrase):
                continue
            # 記号・数字のみ → skip
            if re.match(r'^[\d\s\.\,\-\_\/\\\:\;\!\?「」。、]+$', phrase):
                continue

            phrases.add(phrase)

    return phrases

# ===========================
# 全ファイル処理
# ===========================
def process_files(file_list):
    """ファイルリストを処理してDocument Frequencyを返す"""
    df = Counter()
    for fpath in file_list:
        try:
            text = open(fpath, encoding='utf-8', errors='ignore').read()
        except:
            try:
                text = open(fpath, encoding='cp932', errors='ignore').read()
            except:
                continue
        morphemes = parse_to_morphemes(text)
        phrases = extract_phrases(morphemes)
        df.update(phrases)
    return df

# ===========================
# メイン
# ===========================
def main():
    targets = get_lexical_fn_targets()
    print(f"語彙的FN対象: {len(targets)}件")

    # 語彙的FNファイルのパスリスト
    fn_files = []
    unmatched = []
    for target in sorted(targets):
        fpath = find_file(target, CORPUS_ARCHIVE)
        if fpath:
            fn_files.append(fpath)
        else:
            unmatched.append(target)

    print(f"マッチ成功: {len(fn_files)}件 / 未マッチ: {len(unmatched)}件")
    if unmatched:
        print("未マッチ:", unmatched)

    # 語彙的FNのDF計算
    print("語彙的FNファイル解析中...")
    fn_df = process_files(fn_files)
    print(f"FNユニークフレーズ数: {len(fn_df):,}")

    # 全コーパスのDF計算（FPリスク評価用）
    print("全コーパス解析中...")
    all_files = [
        os.path.join(CORPUS_ARCHIVE, f)
        for f in os.listdir(CORPUS_ARCHIVE)
        if f.lower().endswith('.txt') and f.lower() != 'readme.txt'
    ]
    all_df = process_files(all_files)
    print(f"全コーパスファイル数: {len(all_files)}")

    # 候補生成
    candidates = []
    fn_total = len(fn_files)
    all_total = len(all_files)

    for phrase, fn_count in fn_df.items():
        if fn_count < 3:
            continue
        all_count = all_df.get(phrase, 0)
        if all_count == 0:
            continue
        fp_ratio  = fn_count / all_count
        fn_pct    = fn_count / fn_total * 100
        candidates.append({
            'phrase':   phrase,
            'fn_df':    fn_count,
            'all_df':   all_count,
            'fp_ratio': round(fp_ratio, 3),
            'fn_pct':   round(fn_pct, 1),
            'length':   len(phrase),
        })

    # fp_ratio降順・fn_df降順
    candidates.sort(key=lambda x: (-x['fp_ratio'], -x['fn_df']))

    # CSV出力
    with open(OUTPUT_CSV, 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['phrase','fn_df','all_df','fp_ratio','fn_pct','length'])
        writer.writeheader()
        writer.writerows(candidates)
    print(f"\n出力完了: {OUTPUT_CSV}  ({len(candidates)}件)")

    # ===プレビュー1: FN特異的（fp_ratio≥0.7 & fn_df≥5）===
    print("\n=== FN特異的候補（fp_ratio≥0.7 & fn_df≥5）上位80件 ===")
    print(f"{'フレーズ':20s}  FN件数  全体  FP比率  FN出現率")
    sp = [c for c in candidates if c['fp_ratio'] >= 0.7 and c['fn_df'] >= 5]
    for c in sp[:80]:
        print(f"  {c['phrase']:20s}  {c['fn_df']:4d}  {c['all_df']:4d}  {c['fp_ratio']:.2f}  {c['fn_pct']:4.1f}%")

    # ===プレビュー2: 高頻出（fn_df≥10）===
    print("\n=== 高頻出候補（fn_df≥10）上位50件 ===")
    print(f"{'フレーズ':20s}  FN件数  全体  FP比率  FN出現率")
    hf = sorted(candidates, key=lambda x: -x['fn_df'])
    for c in hf[:50]:
        print(f"  {c['phrase']:20s}  {c['fn_df']:4d}  {c['all_df']:4d}  {c['fp_ratio']:.2f}  {c['fn_pct']:4.1f}%")

    # ===プレビュー3: FP低リスク・中頻出（fp_ratio≥0.6 & fn_df≥8 & length≥6）===
    print("\n=== 辞書候補最有力（fp_ratio≥0.6 & fn_df≥8 & 6文字以上）===")
    print(f"{'フレーズ':20s}  FN件数  全体  FP比率  FN出現率")
    prime = [c for c in candidates
             if c['fp_ratio'] >= 0.6 and c['fn_df'] >= 8 and c['length'] >= 6]
    prime.sort(key=lambda x: (-x['fn_df'], -x['fp_ratio']))
    for c in prime[:50]:
        print(f"  {c['phrase']:20s}  {c['fn_df']:4d}  {c['all_df']:4d}  {c['fp_ratio']:.2f}  {c['fn_pct']:4.1f}%")

if __name__ == '__main__':
    main()
