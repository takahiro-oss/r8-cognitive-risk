#!/usr/bin/env python3
"""
ailabel_analyze.py — AIlabel結果のkappa計算・比較分析ツール

使い方:
  # 単一モデルvshumanのCohen's kappa
  python ailabel/ailabel_analyze.py --results ailabel/results_claude.csv

  # 3モデル統合：Fleiss' kappa + 各モデルのCohen's kappa
  python ailabel/ailabel_analyze.py --results ailabel/results_claude.csv ailabel/results_gemini.csv ailabel/results_gpt4.csv

出力:
  - Fleiss' kappa（3モデル間一致率）
  - Cohen's kappa（各モデル vs human_label）
  - 乖離ケースの一覧
  - ailabel/kappa_results.csv
"""

import argparse
import csv
import sys
from collections import defaultdict

LABEL_ORDER = ["HIGH", "MEDIUM", "LOW", "Intent-Unresolved"]
LABEL_MAP = {l: i for i, l in enumerate(LABEL_ORDER)}


def load_results(csv_path):
    """CSVからAIlabel結果を読み込む"""
    results = {}
    model_name = None
    with open(csv_path, encoding="utf-8-sig") as f:
        for row in csv.DictReader(f):
            target = row["target"].strip()
            model_name = row["model"].strip()
            results[target] = {
                "ai_label": row["ai_label"].strip(),
                "human_label": row["human_label"].strip(),
                "cmi": row["cmi"],
                "r8_level": row["r8_level"],
                "confidence": row.get("confidence", ""),
                "reason": row.get("reason", ""),
            }
    return model_name, results


def cohen_kappa(labels_a, labels_b):
    """Cohen's kappa計算（二者間）"""
    assert len(labels_a) == len(labels_b)
    n = len(labels_a)
    if n == 0:
        return 0.0

    # 観測一致率
    po = sum(1 for a, b in zip(labels_a, labels_b) if a == b) / n

    # 期待一致率
    cats = set(labels_a + labels_b)
    pe = 0.0
    for cat in cats:
        pa = labels_a.count(cat) / n
        pb = labels_b.count(cat) / n
        pe += pa * pb

    if pe >= 1.0:
        return 1.0
    return (po - pe) / (1.0 - pe)


def fleiss_kappa(ratings_matrix, n_raters):
    """Fleiss' kappa計算（3者以上）
    ratings_matrix: list of dict {category: count}
    """
    n_subjects = len(ratings_matrix)
    categories = LABEL_ORDER

    # P_i: 各対象の一致率
    P_i = []
    for row in ratings_matrix:
        total = sum(row.values())
        if total < 2:
            P_i.append(0.0)
            continue
        val = sum(v * (v - 1) for v in row.values())
        P_i.append(val / (total * (total - 1)))

    P_bar = sum(P_i) / n_subjects

    # p_j: 各カテゴリの周辺比率
    p_j = {}
    total_ratings = n_subjects * n_raters
    for cat in categories:
        count = sum(row.get(cat, 0) for row in ratings_matrix)
        p_j[cat] = count / total_ratings

    P_e = sum(v ** 2 for v in p_j.values())

    if P_e >= 1.0:
        return 1.0
    return (P_bar - P_e) / (1.0 - P_e)


def interpret_kappa(k):
    if k < 0:
        return "Poor"
    elif k < 0.20:
        return "Slight"
    elif k < 0.40:
        return "Fair"
    elif k < 0.60:
        return "Moderate"
    elif k < 0.80:
        return "Substantial"
    else:
        return "Almost Perfect"


def main():
    parser = argparse.ArgumentParser(description="AIlabel kappa analysis")
    parser.add_argument("--results", nargs="+", required=True,
                        help="AIlabel結果CSV（1〜3ファイル）")
    parser.add_argument("--out", default="ailabel/kappa_results.csv",
                        help="出力CSVパス")
    args = parser.parse_args()

    # 各CSVを読み込む
    all_models = {}
    for path in args.results:
        model_name, data = load_results(path)
        all_models[model_name] = data
        print(f"読み込み: {path} ({model_name}, {len(data)}件)")

    # 共通targetのみで分析
    all_targets = set.intersection(*[set(d.keys()) for d in all_models.values()])
    all_targets = sorted(all_targets)
    print(f"\n共通target: {len(all_targets)}件\n")

    model_names = list(all_models.keys())

    print("=" * 55)
    print("  Cohen's kappa (各モデル vs human_label)")
    print("=" * 55)

    kappa_results = []
    for model, data in all_models.items():
        ai_labels = []
        human_labels = []
        for t in all_targets:
            ai = data[t]["ai_label"]
            hu = data[t]["human_label"]
            if ai in LABEL_ORDER and hu in LABEL_ORDER:
                ai_labels.append(ai)
                human_labels.append(hu)

        k = cohen_kappa(ai_labels, human_labels)
        interp = interpret_kappa(k)
        print(f"  {model:<40} κ={k:.3f} ({interp})")
        kappa_results.append({"model": model, "kappa_type": "Cohen", "vs": "human_label",
                               "kappa": round(k, 3), "interpretation": interp,
                               "n": len(ai_labels)})

    if len(all_models) >= 2:
        print()
        print("=" * 55)
        print("  Cohen's kappa (モデル間ペア)")
        print("=" * 55)
        model_list = list(all_models.items())
        for i in range(len(model_list)):
            for j in range(i + 1, len(model_list)):
                m1, d1 = model_list[i]
                m2, d2 = model_list[j]
                labels1, labels2 = [], []
                for t in all_targets:
                    a1 = d1[t]["ai_label"]
                    a2 = d2[t]["ai_label"]
                    if a1 in LABEL_ORDER and a2 in LABEL_ORDER:
                        labels1.append(a1)
                        labels2.append(a2)
                k = cohen_kappa(labels1, labels2)
                interp = interpret_kappa(k)
                print(f"  {m1} vs {m2}: κ={k:.3f} ({interp})")
                kappa_results.append({"model": f"{m1} vs {m2}", "kappa_type": "Cohen",
                                       "vs": "inter-model", "kappa": round(k, 3),
                                       "interpretation": interp, "n": len(labels1)})

    if len(all_models) >= 3:
        print()
        print("=" * 55)
        print("  Fleiss' kappa (3モデル間)")
        print("=" * 55)
        ratings_matrix = []
        for t in all_targets:
            row = defaultdict(int)
            for model, data in all_models.items():
                label = data[t]["ai_label"]
                if label in LABEL_ORDER:
                    row[label] += 1
            ratings_matrix.append(dict(row))

        fk = fleiss_kappa(ratings_matrix, len(all_models))
        interp = interpret_kappa(fk)
        print(f"  Fleiss' κ = {fk:.3f} ({interp})")
        kappa_results.append({"model": " / ".join(model_names), "kappa_type": "Fleiss",
                               "vs": "inter-model", "kappa": round(fk, 3),
                               "interpretation": interp, "n": len(ratings_matrix)})

    # 乖離ケース表示
    print()
    print("=" * 55)
    print("  乖離ケース (human vs いずれかのAIラベル)")
    print("=" * 55)
    divergence = []
    for t in all_targets:
        human = list(all_models.values())[0][t]["human_label"]
        ai_labels_dict = {m: d[t]["ai_label"] for m, d in all_models.items()}
        if any(v != human for v in ai_labels_dict.values()):
            row = {"target": t, "human_label": human}
            row.update({f"ai_{m}": v for m, v in ai_labels_dict.items()})
            divergence.append(row)
            ai_str = " / ".join(f"{m}={v}" for m, v in ai_labels_dict.items())
            print(f"  {t}: human={human} | {ai_str}")

    print(f"\n乖離件数: {len(divergence)} / {len(all_targets)}")

    # CSV出力
    import os
    os.makedirs(os.path.dirname(args.out) if os.path.dirname(args.out) else ".", exist_ok=True)
    with open(args.out, "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["model", "kappa_type", "vs", "kappa", "interpretation", "n"])
        writer.writeheader()
        writer.writerows(kappa_results)

    print(f"\nkappa結果を保存: {args.out}")

    # 判定
    print()
    print("=" * 55)
    print("  成功基準との照合（AIlabel_trial_design.md Section 6）")
    print("=" * 55)
    for r in kappa_results:
        if r["kappa_type"] == "Fleiss":
            if r["kappa"] >= 0.40:
                print(f"  Fleiss κ={r['kappa']:.3f} >= 0.40: 基準達成 — criteria はLLMで運用可能")
            else:
                print(f"  Fleiss κ={r['kappa']:.3f} < 0.40: 基準未達 — H-1/H-2は人間判断が必須")
        elif r["vs"] == "human_label":
            if r["kappa"] >= 0.40:
                print(f"  {r['model']} vs human κ={r['kappa']:.3f} >= 0.40: LLMはhuman判断を近似できる")
            else:
                print(f"  {r['model']} vs human κ={r['kappa']:.3f} < 0.40: LLMはhuman判断を近似できない")


if __name__ == "__main__":
    main()
