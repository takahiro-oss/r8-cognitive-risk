import sys
import re

# --- 斉藤監査官専用：実戦型・欺瞞検知辞書 ---
AUTHORITY = ["専門家", "教授", "研究によれば", "大学の研究", "エビデンス", "アナリストチーム", "独自調査"]
HYPE = ["期待される", "可能性がある", "指摘されている", "と言われている", "確実視"]
WARNING_WORDS = ["衝撃", "10倍", "絶対", "損をします", "最後", "大チャンス", "今のうち"]

def analyze_risk(text):
    print("\n" + "="*50)
    print("   R8 Cognitive Risk Analyzer [Ver 3.0 Real-Mode]")
    print("="*50)

    score = 100.0
    detections = []

    # 1. 統計の嘘（分母不明のチェック）
    has_percent = "%" in text or "パーセント" in text
    has_denominator = re.search(r"(N=|分母|調査対象|n=)\d+", text)
    if has_percent and not has_denominator:
        score -= 30.0
        detections.append("[!] 統計リスク: 母集団(N数)が不明なデータで煽っています。")

    # 2. 権威の虎の借（専門家っぽさを装う言葉）
    for word in AUTHORITY:
        if word in text:
            score -= 5.0
            detections.append(f"[!] 権威リスク: '{word}' を使い、断定を避けて信頼させようとしています。")

    # 3. 根拠なき期待（逃げ道を作る言葉）
    for word in HYPE:
        if word in text:
            score -= 5.0
            detections.append(f"[!] 曖昧リスク: '{word}' という言葉で、外れた時の責任を回避しています。")

    # 4. 直接的な煽り（感情操作）
    for word in WARNING_WORDS:
        if word in text:
            score -= 10.0
            detections.append(f"[!] 煽りリスク: '{word}' という強い言葉で冷静な判断を妨げています。")

    # 結果表示
    if not detections:
        print("判定：クリーン（明らかな欺瞞パターンは見当たりません）")
    else:
        for d in detections:
            print(d)

    print("-" * 50)
    final_score = max(0, score)
    print(f"監査スコア : {final_score} / 100")
    print(f"リスク判定 : {'【 要注意 】' if final_score < 70 else '【 安全圏 】'}")
    print("="*50 + "\n")

if __name__ == "__main__":
    target_file = sys.argv[1] if len(sys.argv) > 1 else "t.txt"
    try:
        with open(target_file, "r", encoding="utf-8") as f:
            analyze_risk(f.read())
    except Exception as e:
        print(f"エラー: {e}")