"""
extract_fn_ngrams_v2.py
語彙的FN全件テキストのN-gram頻度分析 改良版

変更点：
- ファイル出現数（document frequency）でカウント → 1ファイル偏在を排除
- ひらがなのみのN-gramを除外 → 助詞・助動詞ノイズを排除
- 最低5文字以上・ひらがな+漢字/カタカナ混在パターンを優先
- ストップワードリストによる除去
- FPリスク評価列を追加（全コーパスでの出現ファイル数との比較）

出力: fn_ngram_candidates_v2.csv
"""

import csv
import os
import re
from collections import Counter, defaultdict

# ===========================
# 設定
# ===========================
CORPUS_ARCHIVE = r"D:\r8_strategy\corpus\phase2\corpus_archive"
SNAPSHOT_CSV   = r"D:\r8_strategy\data\results\corpus_snapshot.csv"
OUTPUT_CSV     = r"D:\r8_strategy\data\results\fn_ngram_candidates_v2.csv"

# ストップワード（助詞・助動詞・汎用表現）
STOPWORDS = {
    "している","ています","っている","てくださ","てください","すること",
    "について","あります","ことが","ことを","ことは","のです","のため",
    "のこと","ません","られる","られた","られて","ている","という",
    "ような","ように","として","において","によって","によって",
    "ながら","なけれ","なければ","であれ","である","ではな","ではない",
    "しかし","そして","また、","また ","さらに","ただし","なので",
    "ですが","ですね","ですよ","ました","ません","します","できる",
    "できた","できて","いない","いる。","いた。","います","いまし",
    "思いま","思って","思うの","思われ","考えら","考えて","考える",
    "ありま","あった","あって","あると","あれば","ある。","ある、",
    "なって","なった","なる。","なると","なれば","なかっ","なかった",
    "場合は","場合に","場合が","場合で","場合も","必要が","必要で",
    "必要は","必要に","必要と","ための","ため、","ため。","こと。",
    "こと、","こと？","こと！","もので","ものが","ものを","ものは",
    "からの","からで","からが","から、","から。","まずは","まず、",
    "さらに","しまう","しまっ","れます","れまし","れてい","れてい",
    "わかる","わかっ","わかり","いただ","いただき","おりま","おります",
    "　　　","、また","。また","もしく","もしくは","もしも",
    "月 日","年 月","年 月 日","月 日 ","年 月 ","年 月 日 ",
    " 月 日"," 年 月"," 年 月 日"," 年 月 日 "," 月 日 ",
    ": : "," : : ","————","—————","——————",
    "ニュース","プロフィール","フォロー","コメント",
    "ください","くださ","ご覧","ご確認",
}

# 現行辞書語彙（除外用・主要なもの）
EXISTING_DICT = {
    "急騰","大急騰","急上昇","爆上げ","今だけ","期間限定","急げ","残りわずか",
    "本日限定","締め切り","今すぐ","最後のチャンス","今が買い時","今のうち",
    "LINE登録","友達追加","限定公開","削除前に","消される前に","以内に削除",
    "絶対","必ず","100%","完全","間違いなく","確実に","全員","誰でも","保証",
    "奇跡","衝撃","感動","驚愕","革命的","人生が変わる","人生が好転",
    "危険","崩壊","破滅","恐怖","脅威","危機","手遅れ","このままでは",
    "衝撃の事実","知らないと損","知らないと危険","の末路","99%が知らない",
    "出会い募集","即会い","恋活","割り切り","真剣な出会い",
    "ほとんどの人が知らない","期待される","可能性がある","かもしれない",
    "激減","劇的に改善","驚異の","鳥肌が立った",
}

# ===========================
# ユーティリティ
# ===========================
def is_meaningful(gram):
    """
    意味のあるN-gram候補かどうかを判定。
    条件：
    - ひらがなのみでない（助詞・助動詞を排除）
    - 数字のみでない
    - ストップワードに含まれない
    - 長さ4〜12文字
    - 既存辞書に含まれない
    """
    if gram in STOPWORDS or gram in EXISTING_DICT:
        return False
    if len(gram) < 4 or len(gram) > 12:
        return False
    # ひらがなのみ → 除外
    if re.match(r'^[\u3040-\u309f、。\s　]+$', gram):
        return False
    # 数字・記号のみ → 除外
    if re.match(r'^[\d\s\.\,\-\_\/\\\:\;\!\?\(\)\[\]\{\}\|＊※◆●■▼▶︎→←↑↓①②③]+$', gram):
        return False
    # スペース・記号だらけ → 除外
    non_space = re.sub(r'[\s　\-\_\/\\\:\;\!\?\(\)\[\]\{\}\|]', '', gram)
    if len(non_space) < 3:
        return False
    return True

def clean_text(text):
    """テキストの前処理"""
    text = re.sub(r'https?://\S+', '', text)          # URL除去
    text = re.sub(r'<[^>]+>', '', text)                # HTMLタグ除去
    text = re.sub(r'[a-zA-Z0-9]{4,}', ' ', text)      # 長い英数字列除去
    text = re.sub(r'[ \t]+', ' ', text)                # 空白正規化
    return text

def extract_ngrams_from_text(text, min_n=4, max_n=10):
    """テキストからN-gramを抽出（文節単位でスライド）"""
    text = clean_text(text)
    ngrams = set()  # 同一ファイル内の重複はsetで除去
    # 文境界でセグメント分割
    segments = re.split(r'[。！？\n\r「」『』【】〔〕]', text)
    for seg in segments:
        seg = seg.strip()
        if len(seg) < min_n:
            continue
        for n in range(min_n, min(max_n + 1, len(seg) + 1)):
            for i in range(len(seg) - n + 1):
                gram = seg[i:i+n]
                if is_meaningful(gram):
                    ngrams.add(gram)
    return ngrams

def find_file(target, archive_dir):
    """targetキーワードを含むファイルをarchive_dirから検索"""
    tl = target.lower().replace(' ', '')
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

# ===========================
# 全コーパスでのDF取得（FPリスク評価用）
# ===========================
def get_all_corpus_files(archive_dir):
    """archive内の全txtファイルパスを返す"""
    files = []
    for fname in os.listdir(archive_dir):
        if fname.lower().endswith('.txt') and fname.lower() != 'readme.txt':
            files.append(os.path.join(archive_dir, fname))
    return files

# ===========================
# メイン処理
# ===========================
def main():
    targets = get_lexical_fn_targets()
    print(f"語彙的FN対象: {len(targets)}件")

    # ステップ1: 語彙的FNファイルからN-gram抽出（Document Frequency）
    fn_df = Counter()   # gram → FNファイル中での出現ファイル数
    matched = 0
    unmatched = []

    for target in sorted(targets):
        fpath = find_file(target, CORPUS_ARCHIVE)
        if fpath is None:
            unmatched.append(target)
            continue
        matched += 1
        try:
            text = open(fpath, encoding='utf-8', errors='ignore').read()
        except:
            try:
                text = open(fpath, encoding='cp932', errors='ignore').read()
            except:
                continue
        grams = extract_ngrams_from_text(text)
        fn_df.update(grams)

    print(f"マッチ成功: {matched}件 / 未マッチ: {len(unmatched)}件")
    if unmatched:
        print("未マッチ:", unmatched)

    # ステップ2: 全コーパスでのDF取得（FPリスク評価）
    print("全コーパスDF計算中...")
    all_files = get_all_corpus_files(CORPUS_ARCHIVE)
    all_df = Counter()
    for fpath in all_files:
        try:
            text = open(fpath, encoding='utf-8', errors='ignore').read()
        except:
            try:
                text = open(fpath, encoding='cp932', errors='ignore').read()
            except:
                continue
        grams = extract_ngrams_from_text(text)
        all_df.update(grams)
    print(f"全コーパスファイル数: {len(all_files)}")

    # ステップ3: FP比率計算 → 候補絞り込み
    # FN_DF / ALL_DF が高い → FNに特異的 → FP低リスク
    # FN_DF / ALL_DF が低い → 全般的に出現 → FP高リスク
    candidates = []
    for gram, fn_count in fn_df.most_common():
        if fn_count < 3:
            continue
        all_count = all_df.get(gram, 0)
        if all_count == 0:
            continue
        fp_ratio = fn_count / all_count   # 1.0に近いほどFNに特異的
        candidates.append({
            'ngram': gram,
            'fn_df': fn_count,
            'all_df': all_count,
            'fp_ratio': round(fp_ratio, 3),
            'fn_pct': round(fn_count / matched * 100, 1),
        })

    # fp_ratio降順・fn_df降順でソート
    candidates.sort(key=lambda x: (-x['fp_ratio'], -x['fn_df']))

    # CSV出力
    with open(OUTPUT_CSV, 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['ngram','fn_df','all_df','fp_ratio','fn_pct'])
        writer.writeheader()
        writer.writerows(candidates)

    print(f"\n出力完了: {OUTPUT_CSV}  ({len(candidates)}件)")

    # プレビュー：FN特異的上位（fp_ratio >= 0.7 かつ fn_df >= 5）
    print("\n=== FN特異的候補（fp_ratio≥0.7 & fn_df≥5）上位60件 ===")
    print(f"{'N-gram':15s}  FN件数  全体件数  FP比率  FN出現率")
    high_specificity = [c for c in candidates if c['fp_ratio'] >= 0.7 and c['fn_df'] >= 5]
    for c in high_specificity[:60]:
        print(f"  {c['ngram']:15s}  {c['fn_df']:4d}    {c['all_df']:4d}    {c['fp_ratio']:.2f}   {c['fn_pct']:4.1f}%")

    print("\n=== 高頻出候補（fn_df≥10 問わずfp_ratio）上位30件 ===")
    print(f"{'N-gram':15s}  FN件数  全体件数  FP比率  FN出現率")
    high_freq = sorted(candidates, key=lambda x: -x['fn_df'])
    for c in high_freq[:30]:
        print(f"  {c['ngram']:15s}  {c['fn_df']:4d}    {c['all_df']:4d}    {c['fp_ratio']:.2f}   {c['fn_pct']:4.1f}%")

if __name__ == '__main__':
    main()
