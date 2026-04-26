#!/usr/bin/env python3
"""
archive_scanned.py — 分析済みファイルをsample_archiveに移動

使い方:
  python archive_scanned.py data/results/scan_20260426.csv

動作:
  CSVのtarget列からscan/内のファイルパスを取得
  ファイルのタイムスタンプ（更新日時）から年月フォルダを判定
  corpus/phase2/sample_archive/YYYY_MM/ に移動
"""

import os
import sys
import csv
import shutil
from datetime import datetime

BASE_DIR    = os.path.dirname(os.path.abspath(__file__))
SCAN_DIR    = os.path.join(BASE_DIR, "corpus", "phase2", "scan")
ARCHIVE_DIR = os.path.join(BASE_DIR, "corpus", "phase2", "sample_archive")


def main():
    if len(sys.argv) < 2:
        print("使い方: python archive_scanned.py <CSVパス>")
        sys.exit(1)

    csv_path = sys.argv[1]
    if not os.path.exists(csv_path):
        print(f"[Error] CSVが見つかりません: {csv_path}")
        sys.exit(1)

    moved   = []
    skipped = []

    with open(csv_path, encoding="utf-8-sig", errors="ignore") as f:
        reader = csv.DictReader(f)
        for row in reader:
            target = row.get("target", "").strip()
            if not target:
                continue

            # scan/内のファイルのみ対象
            fname = os.path.basename(target)
            src   = os.path.join(SCAN_DIR, fname)
            if not os.path.exists(src):
                skipped.append(fname)
                continue

            # タイムスタンプから年月フォルダを決定
            mtime   = os.path.getmtime(src)
            ym      = datetime.fromtimestamp(mtime).strftime("%Y_%m")
            dst_dir = os.path.join(ARCHIVE_DIR, ym)
            os.makedirs(dst_dir, exist_ok=True)

            shutil.move(src, os.path.join(dst_dir, fname))
            moved.append(fname)
            print(f"[OK] {fname} -> sample_archive/{ym}/")

    print(f"\n完了: {len(moved)}件移動 / {len(skipped)}件スキップ")
    if skipped:
        print("スキップ（scan/に存在しない）:")
        for f in skipped:
            print(f"  {f}")


if __name__ == "__main__":
    main()
