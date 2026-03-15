#!/usr/bin/env python3
# r8_simulation.py — R8プロジェクト モンテカルロシミュレーション
# 財務タイムライン内に「最初の有意な接触」が起きる確率を推定する

import random
import statistics

# ===========================
# パラメータ設定
# ===========================

# 財務タイムライン
MONTHS = 10.5

# 月次確率（各イベントが起きる確率）
P_SOCARXIV      = 0.90  # 2ヶ月以内にSocArXiv登録できる確率
P_NOTE_REVENUE  = 0.60  # 3ヶ月以内にnote収益化できる確率
P_DISCOVERY     = 0.05  # 月次：登録後に研究者に発見される確率
P_CITATION      = 0.30  # 発見後：引用される確率
P_CONTACT       = 0.20  # 引用後：問い合わせが来る確率
P_ENGLISH       = 0.70  # 6ヶ月以内に英語版note公開できる確率

# 英語版公開後の発見確率倍率
ENGLISH_MULTIPLIER = 3.0

# シミュレーション回数
TRIALS = 100000

# ===========================
# シミュレーション
# ===========================

def run_trial():
    """
    1回のシミュレーション。
    財務タイムライン内に「問い合わせ」が来るかどうかを返す。
    """
    month = 0.0

    # SocArXiv登録
    if random.random() > P_SOCARXIV:
        return False, None  # 登録できず終了
    month += random.uniform(1, 2)  # 1〜2ヶ月で登録

    if month > MONTHS:
        return False, None

    # 英語版公開
    english_published = False
    english_month = random.uniform(3, 6)
    if random.random() < P_ENGLISH:
        english_published = True

    # 月次で発見→引用→問い合わせの連鎖をシミュレート
    current_month = month
    while current_month <= MONTHS:

        # 発見確率（英語版公開後は倍率適用）
        discovery_prob = P_DISCOVERY
        if english_published and current_month >= english_month:
            discovery_prob = min(P_DISCOVERY * ENGLISH_MULTIPLIER, 0.30)

        if random.random() < discovery_prob:
            # 引用
            if random.random() < P_CITATION:
                # 問い合わせ
                if random.random() < P_CONTACT:
                    return True, current_month

        current_month += 1

    return False, None

# ===========================
# 実行
# ===========================

successes = 0
success_months = []

for _ in range(TRIALS):
    result, month = run_trial()
    if result:
        successes += 1
        success_months.append(month)

success_rate = successes / TRIALS * 100

print("=" * 55)
print("  R8プロジェクト モンテカルロシミュレーション")
print(f"  試行回数: {TRIALS:,}回")
print("=" * 55)
print(f"\n  財務タイムライン内（{MONTHS}ヶ月）に")
print(f"  最初の有意な接触が起きる確率:")
print(f"\n  >>> {success_rate:.1f}% <<<\n")

if success_months:
    print(f"  接触が起きた場合の平均月数: {statistics.mean(success_months):.1f}ヶ月")
    print(f"  最速:  {min(success_months):.1f}ヶ月")
    print(f"  中央値: {statistics.median(success_months):.1f}ヶ月")
    print(f"  最遅:  {max(success_months):.1f}ヶ月")

print("\n" + "-" * 55)
print("  感度分析：各変数の影響度")
print("-" * 55)

# 感度分析：英語版公開の影響
successes_no_english = 0
for _ in range(TRIALS):
    month = random.uniform(1, 2)
    if month > MONTHS:
        continue
    current_month = month
    while current_month <= MONTHS:
        if random.random() < P_DISCOVERY:
            if random.random() < P_CITATION:
                if random.random() < P_CONTACT:
                    successes_no_english += 1
                    break
        current_month += 1

rate_no_english = successes_no_english / TRIALS * 100
print(f"  英語版なしの場合:      {rate_no_english:.1f}%")
print(f"  英語版ありの場合:      {success_rate:.1f}%")
print(f"  英語版による上昇幅:    +{success_rate - rate_no_english:.1f}%")

# 感度分析：SocArXiv登録を1ヶ月早めた場合
successes_early = 0
for _ in range(TRIALS):
    month = random.uniform(0.5, 1.0)  # 早める
    english_published = random.random() < P_ENGLISH
    english_month = random.uniform(3, 6)
    current_month = month
    while current_month <= MONTHS:
        discovery_prob = P_DISCOVERY
        if english_published and current_month >= english_month:
            discovery_prob = min(P_DISCOVERY * ENGLISH_MULTIPLIER, 0.30)
        if random.random() < discovery_prob:
            if random.random() < P_CITATION:
                if random.random() < P_CONTACT:
                    successes_early += 1
                    break
        current_month += 1

rate_early = successes_early / TRIALS * 100
print(f"\n  SocArXiv登録を1ヶ月早めた場合: {rate_early:.1f}%")
print(f"  上昇幅: +{rate_early - success_rate:.1f}%")

print("\n" + "=" * 55)
print("  [注意] このシミュレーションは探索的なものです。")
print("  変数の設定は理論的推論に基づく仮定値です。")
print("  予測ではなく感度分析として使用してください。")
print("=" * 55)
