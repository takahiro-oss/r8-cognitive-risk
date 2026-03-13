#!/usr/bin/env python3
"""
R8 Mass Audit - 複数ファイル・URLの一括分析
使い方: python mass_audit.py targets.csv
"""

import csv
import json
import sys
import os
import re
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import r8

WEIGHTS = {
    "authority": 0.08,
    "emotional": 0.15,
    "logical": 0.10,
    "statistical": 0.08,
    "hype": 0.15,
    "clickbait": 0.12,
    "propaganda": 0.12,
    "fear": 0.08,
    "enemy_frame": 0.05,
    "disclaimer_exploit": 0.02,
    "anonymous_authority": 0.03,
    "naked_number": 0.02
}

THRESHOLDS = {
    "authority": 0.3,
    "emotional": 0.3,
    "logical": 0.3,
    "statistical": 0.5,
    "hype": 0.2,
    "clickbait": 0.2,
    "propaganda": 0.2,
    "fear": 0.3,
    "enemy_frame": 0.2,
    "disclaimer_exploit": 1.0,
    "anonymous_authority": 1.0,
    "naked_number": 1.0
}


def get_text(source):
    if source.startswith("http"):
        import urllib.request
        req = urllib.request.Request(
            source,
            headers={"User-Agent": "Mozilla/5.0"}
        )
        with urllib.request.urlopen(req, timeout=15) as res:
            raw_bytes = res.read()
        try:
            import chardet
            enc = chardet.detect(raw_bytes)["encoding"] or "utf-8"
        except ImportError:
            enc = "utf-8"
        text = raw_bytes.decode(enc, errors="ignore")
        # HTMLタグ除去
        text = re.sub(r"<[^>]+>", " ", text)
        return text
    elif source.lower().endswith(".pdf"):
        try:
            import fitz
            doc = fitz.open(source)
            return "\n".join(page.get_text() for page in doc)
        except Exception as e:
            raise RuntimeError(f"PDF読み込み失敗: {e}")
    else:
        with open(source, encoding="utf-8") as f:
            return f.read()


def calc_score(result):
    ri = {cat: min(result.get(cat, 0) / THRESHOLDS[cat], 1.0) for cat in WEIGHTS}
    penalty = sum(WEIGHTS[c] * ri[c] * 100 for c in WEIGHTS)
    score = max(0.0, round(100 - penalty, 1))
    risk = "high" if score < 40 else "medium" if score < 70 else "low"
    return score, risk


def analyze_one(row):
    source = row.get("source", "").strip()
    label = row.get("label", "").strip()
    note = row.get("note", "").strip()

    try:
        text = get_text(source)
        result = r8.analyze(text)
        score, risk = calc_score(result)
        return {
            "source": source,
            "label": label,
            "note": note,
            "score": score,
            "risk": risk,
            "status": "ok",
            "detail": result
        }
    except Exception as e:
        return {
            "source": source,
            "label": label,
            "note": note,
            "score": None,
            "risk": None,
            "status": f"error: {e}",
            "detail": {}
        }


def main():
    if len(sys.argv) < 2:
        print("使い方: python mass_audit.py targets.csv")
        sys.exit(1)

    targets_path = sys.argv[1]
    output_base = sys.argv[2] if len(sys.argv) > 2 else "audit_results"

    with open(targets_path, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    print(f"対象: {len(rows)}件")

    results = []
    with ThreadPoolExecutor(max_workers=2) as executor:
        futures = {executor.submit(analyze_one, row): row for row in rows}
        for i, future in enumerate(as_completed(futures), 1):
            res = future.result()
            results.append(res)
            score = res["score"] if res["score"] is not None else "-"
            print(f"[{i}/{len(rows)}] {res['source'][:50]} | score={score} | {res['status']}")

    csv_path = output_base + ".csv"
    with open(csv_path, "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["source", "label", "note", "score", "risk", "status"])
        writer.writeheader()
        for r in results:
            writer.writerow({k: r[k] for k in ["source", "label", "note", "score", "risk", "status"]})

    json_path = output_base + ".json"
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump({
            "generated": datetime.now().isoformat(),
            "total": len(results),
            "results": results
        }, f, ensure_ascii=False, indent=2)

    print(f"\n完了 → {csv_path} / {json_path}")


if __name__ == "__main__":
    main()