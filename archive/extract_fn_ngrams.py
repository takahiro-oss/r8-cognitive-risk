"""
extract_fn_ngrams.py
語彙的FN全件テキストのN-gram頻度分析 → 辞書追加候補抽出
出力: fn_ngram_candidates.csv
"""

import csv
import os
import re
from collections import Counter

# ===========================
# 設定
# ===========================
CORPUS_ARCHIVE = r"D:\r8_strategy\corpus\phase2\corpus_archive"
SNAPSHOT_CSV   = r"D:\r8_strategy\data\results\corpus_snapshot.csv"
OUTPUT_CSV     = r"D:\r8_strategy\data\results\fn_ngram_candidates.csv"

# 現行辞書語彙（r8.py から転記 ― ヒット済み語彙を除外するため）
EXISTING_DICT = set([
    # HYPE
    "急騰","大急騰","急騰目前","急上昇","爆上げ","期待される","可能性がある",
    "指摘されている","と言われている","確実視","見込まれる","予想される","とも言える",
    "かもしれない","といわれています","とされています","という考え方があります",
    "体感される方が多い","感じる方もいます","つながると言われ","宇宙からのメッセージ",
    "サインかもしれません","暗示しています","スピリチュアル的には","霊的に見ると",
    "魂レベルでは","エネルギー的に","波動的に","高次元では","激減","劇的に改善",
    "驚異の","奇跡の","たった3ヶ月で","99%の人が","ほとんどの人が知らない",
    "知らなきゃ損","鳥肌が立った","眠れなくなる","震えが止まらない",
    # URGENCY
    "一度しか言いません","必ず買うべき","スーパーインサイダー","一攫千金","今だけ",
    "期間限定","急げ","残りわずか","本日限定","締め切り","今すぐ","最後のチャンス",
    "今が買い時","今のうち","LINEはこちら","LINE追加","LINEで受け取る","LINE登録",
    "IDはこちら","DMください","気軽にDM","まずはDM","無料で受け取る","無料配布中",
    "今すぐ登録","登録はこちら","友達追加","限定公開","シークレット",
    "8時間後に削除","25分後に削除","今週限り","今だけ公開","削除前に","消される前に",
    "以内に削除","日後に消","時間で消","時間後に消します","日以内に消します",
    # ABSOLUTIST
    "絶対","必ず","100%","完全","間違いなく","確実に","全員","誰でも","保証",
    "副作用が全くない","どんな病気にも","必ず引き寄せられる","どんな症状にも効く",
    "年齢を問わない","安全で効果的","好転反応","再現性がある","細胞レベルで回復",
    "必ず買い","今すぐやれ","一度だけ言う","命の危険を冒して","1億回でも言います",
    "本っっ当に大事","ゾッとした","衝撃展開","死ぬまで働け","のーはありえない",
    # EMOTIONAL
    "奇跡","衝撃","感動","驚愕","革命的","人生が変わる","夢の","覚醒","次元上昇",
    "魂","引き寄せ","潜在意識","使命","ツインレイ","ツインソウル","宇宙の法則",
    "光の存在","愛のエネルギー","スターシード","ライトワーカー","ミラクル","奇跡的回復",
    "人生が好転","運命の人","カルマ","前世","守護霊","魂の覚醒","ソウルメイト",
    "エンジェル","グラウンディング","次元","神聖","サイン","シンクロニシティ",
    "お金以上のもの","ありがとうを集める",
    # FEAR
    "危険","崩壊","破滅","恐怖","脅威","危機","標準治療では治らない","副反応","余命",
    "手遅れ","このままでは","悪化する一方","西洋医学の限界","抗がん剤の毒性",
    "ワクチンの危険","国が滅びる","日本終わる","手遅れになる","取り返しがつかない",
    "侵略される","乗っ取られる","消滅する","存亡の危機","外国人に占領","文化が破壊",
    "伝統が失われる","子孫に申し訳ない","人類が滅びる","文明がリセット","核攻撃",
    "世界が終わる","闇の勢力に支配","人口が削減される","マイクロチップで管理",
    "電磁波攻撃","5Gで洗脳","監視社会が来る",
    # CLICKBAIT
    "衝撃の事実","絶対に見て","知らないと損","閲覧注意","知らないと危険",
    "見逃してはいけない","今すぐ確認","衝撃の真実","99%が知らない","医師が隠す",
    "公式が認めない","の末路",
    # SEXUAL
    "せふれ","おふぱこ","わんないと","出会い募集","即会い","写真交換","動画送ります",
    "体の関係","大人の関係","ご縁があれば","気軽にメッセージ","IDを教えます",
    "LINE教えます","仲良くしたい","お話しませんか","暇な人DM","気が合う人",
    "大人の友達","割り切り","真剣な出会い","恋活","婚活以外",
])

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
# ファイルマッチング
# ===========================
def find_file(target, archive_dir):
    """targetキーワードを含むファイルを検索（大文字小文字無視）"""
    tl = target.lower().replace('_', '')
    for fname in os.listdir(archive_dir):
        if fname.lower() == 'readme.txt':
            continue
        fl = fname.lower().replace('_', '').replace('-', '')
        # 完全前方一致 or stem一致
        stem = os.path.splitext(fl)[0]
        if stem == tl or stem.startswith(tl) or fl.startswith(tl + '.'):
            return os.path.join(archive_dir, fname)
    return None

# ===========================
# N-gram抽出（2〜8文字）
# ===========================
def extract_ngrams(text, min_n=2, max_n=8):
    """
    日本語テキストから文字N-gramを抽出。
    ひらがな・カタカナ・漢字・記号を含むスライド窓。
    URLや英数字のみの部分はスキップ。
    """
    # URL除去
    text = re.sub(r'https?://\S+', '', text)
    # HTMLタグ除去
    text = re.sub(r'<[^>]+>', '', text)
    # 連続する英数字・記号のみのトークンは除去
    text = re.sub(r'[a-zA-Z0-9\s\.\,\!\?\(\)\[\]\{\}\|\-\_\/\\]+', ' ', text)

    ngrams = []
    # 句点・改行でセグメント分割してからN-gram
    segments = re.split(r'[。！？\n「」『』【】\t]', text)
    for seg in segments:
        seg = seg.strip()
        if len(seg) < min_n:
            continue
        for n in range(min_n, max_n + 1):
            for i in range(len(seg) - n + 1):
                gram = seg[i:i+n]
                # スペース・記号だけのものは除外
                if re.match(r'^[\s　、。・]+$', gram):
                    continue
                # 既存辞書に含まれるものは除外
                if gram in EXISTING_DICT:
                    continue
                ngrams.append(gram)
    return ngrams

# ===========================
# メイン処理
# ===========================
def main():
    targets = get_lexical_fn_targets()
    print(f"語彙的FN対象: {len(targets)}件")

    all_ngrams = Counter()
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
        ngrams = extract_ngrams(text)
        all_ngrams.update(ngrams)

    print(f"マッチ成功: {matched}件 / 未マッチ: {len(unmatched)}件")
    if unmatched:
        print("未マッチターゲット:", unmatched)

    # 上位候補を出力（出現2件以上・4文字以上優先）
    print(f"\n総ユニークN-gram: {len(all_ngrams):,}")

    # CSVに書き出し
    with open(OUTPUT_CSV, 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['ngram', 'count', 'length'])
        for gram, cnt in all_ngrams.most_common(2000):
            if cnt >= 3 and len(gram) >= 3:
                writer.writerow([gram, cnt, len(gram)])

    print(f"出力完了: {OUTPUT_CSV}")
    print("\n=== 上位50件プレビュー（4文字以上・3件以上） ===")
    preview = [(g, c) for g, c in all_ngrams.most_common(500)
               if c >= 3 and len(g) >= 4][:50]
    for gram, cnt in preview:
        print(f"  {cnt:4d}回  {gram}")

if __name__ == '__main__':
    main()
