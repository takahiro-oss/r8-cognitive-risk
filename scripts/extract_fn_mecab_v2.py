"""
extract_fn_mecab_v2.py
MeCab形態素解析による語彙的FN辞書候補抽出（著者正規化版）

v1からの変更点：
- 著者正規化：同一著者の複数ファイルをDF計算で1著者1票に集約
- 著者IDはファイル名プレフィックスで判定（note164〜note179 → 著者「ryu」等）
- FP比率計算も著者正規化後のDFで実施
- 著者別の語彙貢献度も出力（どの著者の語彙が多いか可視化）

出力: D:\r8_strategy\data\results\fn_mecab_candidates_v2.csv
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
OUTPUT_CSV     = r"D:\r8_strategy\data\results\fn_mecab_candidates_v2.csv"

tagger = MeCab.Tagger()

TARGET_POS = {'名詞', '動詞', '形容詞', '副詞', '感動詞', '接頭辞'}
SKIP_ONLY_POS = {'助詞', '助動詞', '記号', '補助記号', '空白', '接続詞'}

# 著者グループ定義
# ファイル名の先頭パターンで著者を判定
# 同一著者の複数ファイルはDF計算で1票にキャップ
AUTHOR_PATTERNS = [
    # (正規表現パターン, 著者ID)
    (r'^note1(6[2-9]|7[0-9])\.txt$',   'author_ryu'),        # 弁護士リュウ系（note162〜179）
    (r'^note1(1[1-9]|20|21)\.txt$',    'author_note11x'),    # note111〜121
    (r'^note1(2[2-9]|30)\.txt$',       'author_note12x'),    # note122〜130
    (r'^web2(0[1-9]|1[0-9])\.txt$',    'author_web20x'),     # web201〜219
    (r'^AD_0[3-5]\d',                   'author_ad'),         # AD系広告
    (r'^Web_08[89]|Web_09[14]',         'author_web08x'),     # Web_088〜094
    (r'^note_0[6-9]\d',                 'author_note_old'),   # note_062等旧番号
    (r'^BL_',                           'author_bl'),         # BL系
    (r'^WEB_0[12]\d',                   'author_web_old'),    # WEB_016〜033等
]

def get_author(filename):
    """ファイル名から著者IDを返す。マッチしない場合はファイル名をそのまま返す"""
    fl = filename.lower()
    for pattern, author_id in AUTHOR_PATTERNS:
        if re.match(pattern, fl, re.IGNORECASE):
            return author_id
    # マッチしない場合はファイル名のstemを著者IDとする（1ファイル=1著者）
    return os.path.splitext(fl)[0]

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

NOISE_PATTERNS = [
    r'チップで応援', r'いいなと思ったら', r'フォロー',
    r'コメント', r'シェア', r'プロフィール', r'マガジン',
    r'^\d+$', r'^[a-zA-Z0-9]+$',
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
# MeCabフレーズ抽出
# ===========================
def parse_to_morphemes(text):
    text = re.sub(r'https?://\S+', '', text)
    text = re.sub(r'<[^>]+>', '', text)
    text = re.sub(r'[a-zA-Z0-9]{5,}', '', text)
    morphemes = []
    node = tagger.parseToNode(text)
    while node:
        surface = node.surface
        feature = node.feature.split(',')
        pos = feature[0] if feature else ''
        if surface and pos not in ('BOS/EOS',):
            morphemes.append({'surface': surface, 'pos': pos})
        node = node.next
    return morphemes

def extract_phrases(morphemes, max_len=4):
    phrases = set()
    n = len(morphemes)
    for i in range(n):
        for length in range(1, max_len + 1):
            if i + length > n:
                break
            window = morphemes[i:i+length]
            pos_set = {m['pos'] for m in window}
            if pos_set.issubset(SKIP_ONLY_POS):
                continue
            if not pos_set.intersection(TARGET_POS):
                continue
            phrase = ''.join(m['surface'] for m in window).strip()
            if len(phrase) < 3:
                continue
            if phrase in EXISTING_DICT:
                continue
            if NOISE_RE.search(phrase):
                continue
            if re.match(r'^[\u3040-\u309f]+$', phrase):
                continue
            if re.match(r'^[\d\s\.\,\-\_\/\\\:\;\!\?「」。、・]+$', phrase):
                continue
            phrases.add(phrase)
    return phrases

def read_text(fpath):
    for enc in ('utf-8', 'cp932'):
        try:
            return open(fpath, encoding=enc, errors='ignore').read()
        except:
            continue
    return ''

# ===========================
# 著者正規化DF計算
# ===========================
def compute_author_normalized_df(file_list):
    """
    著者正規化Document Frequency計算。
    同一著者の複数ファイルからのフレーズ貢献を1にキャップする。
    戻り値: {phrase: author_count}
    """
    # author_id → そのauthorが持つphraseのset
    author_phrases = defaultdict(set)

    for fpath in file_list:
        fname = os.path.basename(fpath)
        author = get_author(fname)
        text = read_text(fpath)
        if not text:
            continue
        morphemes = parse_to_morphemes(text)
        phrases = extract_phrases(morphemes)
        author_phrases[author].update(phrases)

    # 著者ごとのphrase setをマージ → phrase: 何著者で出現したか
    df = Counter()
    for author, phrases in author_phrases.items():
        df.update(phrases)

    return df, len(author_phrases)

# ===========================
# メイン
# ===========================
def main():
    targets = get_lexical_fn_targets()
    print(f"語彙的FN対象: {len(targets)}件")

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

    # FNコーパス：著者正規化DF
    print("\n語彙的FNファイル解析中（著者正規化）...")
    fn_df, fn_author_count = compute_author_normalized_df(fn_files)
    print(f"FN著者数（正規化後）: {fn_author_count}")
    print(f"FNユニークフレーズ数: {len(fn_df):,}")

    # 全コーパス：著者正規化DF（FPリスク評価用）
    print("全コーパス解析中（著者正規化）...")
    all_files = [
        os.path.join(CORPUS_ARCHIVE, f)
        for f in os.listdir(CORPUS_ARCHIVE)
        if f.lower().endswith('.txt') and f.lower() != 'readme.txt'
    ]
    all_df, all_author_count = compute_author_normalized_df(all_files)
    print(f"全コーパス著者数（正規化後）: {all_author_count}")

    # 候補生成
    candidates = []
    for phrase, fn_count in fn_df.items():
        if fn_count < 2:   # 著者正規化後は閾値を2以上に下げる
            continue
        all_count = all_df.get(phrase, 0)
        if all_count == 0:
            continue
        fp_ratio = fn_count / all_count
        fn_pct   = fn_count / fn_author_count * 100
        candidates.append({
            'phrase':   phrase,
            'fn_df':    fn_count,
            'all_df':   all_count,
            'fp_ratio': round(fp_ratio, 3),
            'fn_pct':   round(fn_pct, 1),
            'length':   len(phrase),
        })

    candidates.sort(key=lambda x: (-x['fp_ratio'], -x['fn_df']))

    # CSV出力
    with open(OUTPUT_CSV, 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['phrase','fn_df','all_df','fp_ratio','fn_pct','length'])
        writer.writeheader()
        writer.writerows(candidates)
    print(f"\n出力完了: {OUTPUT_CSV}  ({len(candidates)}件)")

    # プレビュー1: FN特異的（fp_ratio=1.0 & fn_df≥3）
    print(f"\n=== FN特異的候補（fp_ratio=1.0 & fn_df≥3・著者正規化後）===")
    print(f"{'フレーズ':22s}  FN著者数  全体著者  FP比率  FN出現率  文字数")
    sp = [c for c in candidates if c['fp_ratio'] == 1.0 and c['fn_df'] >= 3]
    sp.sort(key=lambda x: -x['fn_df'])
    for c in sp[:60]:
        print(f"  {c['phrase']:22s}  {c['fn_df']:5d}    {c['all_df']:5d}    {c['fp_ratio']:.2f}  {c['fn_pct']:5.1f}%  {c['length']:3d}")

    # プレビュー2: 高FN出現率（fn_df≥4 & fp_ratio≥0.6 & length≥5）
    print(f"\n=== 辞書候補最有力（fn_df≥4 & fp_ratio≥0.6 & 5文字以上）===")
    print(f"{'フレーズ':22s}  FN著者数  全体著者  FP比率  FN出現率  文字数")
    prime = [c for c in candidates
             if c['fn_df'] >= 4 and c['fp_ratio'] >= 0.6 and c['length'] >= 5]
    prime.sort(key=lambda x: (-x['fn_df'], -x['fp_ratio']))
    for c in prime[:80]:
        print(f"  {c['phrase']:22s}  {c['fn_df']:5d}    {c['all_df']:5d}    {c['fp_ratio']:.2f}  {c['fn_pct']:5.1f}%  {c['length']:3d}")

if __name__ == '__main__':
    main()
