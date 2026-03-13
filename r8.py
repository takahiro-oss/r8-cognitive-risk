#!/usr/bin/env python3
# r8.py — R8 Cognitive Risk Analyzer v7 (Full Integration)
# 12カテゴリ辞書・構造的欺瞞検出・PDF・YouTube・自動入力判定 すべて搭載

import sys
import re

# --- 外部ライブラリのインポート ---
try:
    from youtube_transcript_api import YouTubeTranscriptApi
    YT_AVAILABLE = True
except ImportError:
    YT_AVAILABLE = False

try:
    import fitz # PyMuPDF
    PDF_ENGINE = "pymupdf"
except ImportError:
    PDF_ENGINE = None

# ===========================
# 12カテゴリ辞書
# ===========================
AUTHORITY_WORDS    = ["専門家","教授","研究によると","科学的に証明","大学の研究","博士","学者","権威","エビデンス","論文","研究者","機関","医師","臨床","実証済み","データが示す","調査によれば","アナリストチーム","独自調査","研究によれば"]
HYPE_WORDS         = ["期待される","可能性がある","確実視","見込まれる","予想される","絶対","必ず","間違いない","保証","驚異的","奇跡","劇的","衝撃","革命的","前代未聞","史上最強","今だけ","限定","秘密","暴露"]
URGENCY_WORDS      = ["今すぐ","急いで","限定","残りわずか","期間限定","締め切り","今だけ","急騰","緊急","本日限定","最後のチャンス","今が買い時","今のうち"]
ABSOLUTIST_WORDS   = ["絶対","必ず","100%","完全","間違いなく","確実に","全員","誰でも","保証"]
EMOTIONAL_WORDS    = ["奇跡","衝撃","感動","驚愕","革命的","人生が変わる","夢の"]
FEAR_WORDS         = ["危険","崩壊","破滅","恐怖","脅威","危機","末期","手遅れ","もう限界","滅亡","支配","監視","抹殺","闇","陰謀"]
ANECDOTAL_MARKERS  = ["私の場合","体験談","友人が","実際に試した","お客様の声"]
STATISTICAL_WORDS  = ["累計","最大","平均","No.1","利用者数","成功率","合格率","改善率","実績"]
CONCLUSION_MARKERS = ["だから","つまり","したがって","結果として","以上より","当然","明らかに"]
CLICKBAIT_WORDS    = ["衝撃の事実","絶対に見て","知らないと損","閲覧注意"]
PROPAGANDA_WORDS   = ["メディアは嘘","誰も言わない","裏の勢力","洗脳","真実を知れ","目覚めよ","ディープステート","グローバリスト","ワクチン","マインドコントロール","覚醒","波動","次元上昇","宇宙の意思","引き寄せ","エネルギー","潜在意識"]
ENEMY_FRAME        = ["敵","支配","騙されている","操作されている"]
ALLY_FRAME         = ["我々","みんな","国民","真実を知る人"]
DISCLAIMER_WORDS   = ["投資助言ではありません","損失の責任","情報提供および教育目的","投資顧問として","元本を失う可能性","将来の成果を保証","デューデリジェンス"]
ANONYMOUS_SUBJECT  = ["当社","一部のアナリスト","市場では","業界では","関係者によると","一部で","見方が出ている","強気の買い判断","目標株価を示す"]

# ===========================
# 重み付けと閾値
# ===========================
THRESHOLDS = {
    "authority": 0.05, "emotional": 0.08, "logical": 0.04, "statistical": 0.06,
    "hype": 0.05, "clickbait": 0.04, "propaganda": 0.04, "fear": 0.05,
    "enemy_frame": 0.04, "disclaimer_exploit": 0.30,
    "anonymous_authority": 0.30, "naked_number": 0.30,
}
WEIGHTS = {
    "authority": 0.12, "emotional": 0.12, "logical": 0.08, "statistical": 0.16,
    "hype": 0.08, "clickbait": 0.04, "propaganda": 0.04, "fear": 0.08,
    "enemy_frame": 0.08, "disclaimer_exploit": 0.08,
    "anonymous_authority": 0.06, "naked_number": 0.06,
}
CATEGORY_LABELS = {
    "authority":           "Authority Risk        (権威リスク)",
    "emotional":           "Emotional Risk        (感情誘導リスク)",
    "logical":             "Logical Risk          (論理飛躍リスク)",
    "statistical":         "Statistical Risk      (統計操作リスク) ★",
    "hype":                "Hype Risk             (責任回避型煽りリスク)",
    "clickbait":           "Clickbait Risk        (クリックベイト)",
    "propaganda":          "Propaganda Risk       (プロパガンダ)",
    "fear":                "Fear Risk             (恐怖煽動リスク)",
    "enemy_frame":         "Enemy Frame           (敵/味方フレーム)",
    "disclaimer_exploit":  "Disclaimer Exploit    (免責文逆利用) ★",
    "anonymous_authority": "Anonymous Authority   (匿名権威)",
    "naked_number":        "Naked Number          (根拠なき具体数値)",
}

# ===========================
# 取得・分析ロジック
# ===========================
def density(text, words):
    if not text: return 0.0
    count = sum(text.count(w) for w in words)
    return count / (len(text) / 100)

def bar(v, width=20):
    filled = max(0, min(width, round(v * width)))
    return "[" + "█" * filled + "░" * (width - filled) + f"] {v:.2f}"

def get_text(target):
    if "youtube.com" in target or "youtu.be" in target:
        if not YT_AVAILABLE: return "[Error] youtube-transcript-api がありません"
        vid_match = re.search(r"(?:v=|\/)([0-9A-Za-z_-]{11})", target)
        if not vid_match: return "[Error] YouTube URL 不正"
        vid = vid_match.group(1)
        try:
            ts = YouTubeTranscriptApi.get_transcript(vid, languages=["ja", "en"])
            print("YouTube字幕取得完了\n")
            return " ".join([x["text"] for x in ts])
        except Exception as e:
            return f"[Error] 字幕取得失敗: {e}"

    if target.lower().endswith(".pdf"):
        if not PDF_ENGINE: return "[Error] PDF用ライブラリ(PyMuPDF)がありません"
        try:
            doc = fitz.open(target)
            return "\n".join(page.get_text() for page in doc)
        except Exception as e:
            return f"[Error] PDF読み込み失敗: {e}"

    try:
        with open(target, "r", encoding="utf-8", errors="ignore") as f:
            return f.read()
    except FileNotFoundError:
        return f"[Error] ファイル未検出: {target}"

def analyze(text):
    raw = {
        "authority": density(text, AUTHORITY_WORDS),
        "emotional": (density(text, URGENCY_WORDS) + density(text, ABSOLUTIST_WORDS) + density(text, EMOTIONAL_WORDS)) / 3,
        "logical": density(text, ANECDOTAL_MARKERS + CONCLUSION_MARKERS),
        "statistical": density(text, STATISTICAL_WORDS) + (len(re.findall(r"\d+%", text)) / 10),
        "hype": density(text, HYPE_WORDS),
        "clickbait": density(text, CLICKBAIT_WORDS),
        "propaganda": density(text, PROPAGANDA_WORDS),
        "fear": density(text, FEAR_WORDS),
        "enemy_frame": density(text, ENEMY_FRAME + ALLY_FRAME),
        "disclaimer_exploit": 0.8 if (density(text, DISCLAIMER_WORDS) > 0.1 and density(text, HYPE_WORDS) > 0.1) else 0.0,
        "anonymous_authority": min(density(text, ANONYMOUS_SUBJECT) * 2, 1.0),
        "naked_number": 0.8 if (re.search(r"\d+倍|\d+円", text) and not re.search(r"出典|引用", text)) else 0.0,
        "_structure": round(density(text, ["なぜなら", "原因", "解決"]) / 3, 3),
        "_sentiment_bias": round(abs(density(text, EMOTIONAL_WORDS) - density(text, FEAR_WORDS)), 3)
    }
    return raw

def report(text, source):
    raw = analyze(text)
    ri = {cat: min(raw.get(cat, 0) / THRESHOLDS[cat], 1.0) for cat in WEIGHTS}
    penalty = sum(WEIGHTS[c] * ri[c] * 100 for c in WEIGHTS)
    score = max(0.0, round(100 - penalty, 1))
    print("\n" + "=" * 50)
    print(f"  R8 Analyzer v7 | Source: {source[:40]}")
    print("=" * 50)
    print(f"  Score: {score} / 100")
    print("-" * 50)
    for cat, lbl in CATEGORY_LABELS.items():
        print(f"  {lbl}\n    {bar(ri[cat])}")
    print("-" * 50)
    print("\n[Notice] R8は認知リスクのフラグ提示ツールです。")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("使い方: python r8.py <URL/File>")
        sys.exit(1)
    target = sys.argv[1]
    content = get_text(target)
    if content.startswith("[Error]"):
        print(content)
    else:
        report(content, target)