import os
import glob

results_dir = 'D:/r8_strategy/data/results'
out_file = f'{results_dir}/phase2_20260404.csv'

csv_files = sorted(glob.glob(f'{results_dir}/AD_*_20260404.csv'))

header = None
rows = []

for fpath in csv_files:
    with open(fpath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    if not header:
        header = lines[0]
    for line in lines[1:]:
        if line.strip():
            rows.append(line)

with open(out_file, 'w', encoding='utf-8') as f:
    f.write(header)
    f.writelines(rows)

print(f"統合完了: {len(rows)}件 → {out_file}")
for r in rows:
    parts = r.split(',')
    print(f"  {parts[1].split('/')[-1]}  CMI:{parts[2]}  [{parts[3]}]")
