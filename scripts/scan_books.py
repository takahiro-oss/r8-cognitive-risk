# -*- coding: utf-8 -*-
import subprocess, sys, csv
from datetime import datetime

timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

targets = [
    (r'corpus\book\butinukutikara\1\u7ae0.txt', 'yozawa_butinuku_ch1'),
    (r'corpus\book\butinukutikara\2\u7ae0.txt', 'yozawa_butinuku_ch2'),
    (r'corpus\book\butinukutikara\3\u7ae0.txt', 'yozawa_butinuku_ch3'),
    (r'corpus\book\butinukutikara\4\u7ae0.txt', 'yozawa_butinuku_ch4'),
    (r'corpus\book\butinukutikara\5\u7ae0.txt', 'yozawa_butinuku_ch5'),
    (r'corpus\book\butinukutikara\6\u7ae0.txt', 'yozawa_butinuku_ch6'),
    (r'corpus\book\byousokude_itiokuenkasegujouken\1\u7ae0.txt', 'yozawa_byousoku_ch1'),
    (r'corpus\book\byousokude_itiokuenkasegujouken\2\u7ae0.txt', 'yozawa_byousoku_ch2'),
    (r'corpus\book\byousokude_itiokuenkasegujouken\3\u7ae0.txt', 'yozawa_byousoku_ch3'),
    (r'corpus\book\byousokude_itiokuenkasegujouken\4\u7ae0.txt', 'yozawa_byousoku_ch4'),
    (r'corpus\book\byousokude_itiokuenkasegujouken\5\u7ae0.txt', 'yozawa_byousoku_ch5'),
    (r'corpus\book\byousokude_itiokuenkasegujouken\6\u7ae0.txt', 'yozawa_byousoku_ch6'),
    (r'corpus\book\byousokude_itiokuenkasegujouken\7\u7ae0.txt', 'yozawa_byousoku_ch7'),
    (r'corpus\book\kimiwanazehatarakuka\ch1.txt', 'watanabe_kimi_ch1'),
    (r'corpus\book\kimiwanazehatarakuka\ch2.txt', 'watanabe_kimi_ch2'),
    (r'corpus\book\kimiwanazehatarakuka\ch3.txt', 'watanabe_kimi_ch3'),
    (r'corpus\book\kimiwanazehatarakuka\ch4.txt', 'watanabe_kimi_ch4'),
    (r'corpus\book\kimiwanazehatarakuka\ch5.txt', 'watanabe_kimi_ch5'),
    (r'corpus\book\kimiwanazehatarakuka\ch6.txt', 'watanabe_kimi_ch6'),
    (r'corpus\book\kyouikunohoukai\ch1.txt', 'watanabe_kyoiku_ch1'),
    (r'corpus\book\kyouikunohoukai\ch2.txt', 'watanabe_kyoiku_ch2'),
    (r'corpus\book\kyouikunohoukai\ch3.txt', 'watanabe_kyoiku_ch3'),
    (r'corpus\book\kyouikunohoukai\ch4.txt', 'watanabe_kyoiku_ch4'),
    (r'corpus\book\kyouikunohoukai\ch5.txt', 'watanabe_kyoiku_ch5'),
]

out_path = r'data\results\scan_books.csv'
header = ['timestamp','target','cmi','level','error','authority','emotional','logical',
          'statistical','hype','clickbait','propaganda','fear','enemy_frame',
          'disclaimer_exploit','anonymous_authority','naked_number','sexual_induction',
          'beauty_diet','human_label','riskfactor']

rows = []
for filepath, short_name in targets:
    print('scanning: ' + short_name + ' ...', end=' ', flush=True)
    result = subprocess.run(
        [sys.executable, 'r8.py', filepath, '--format', 'csv'],
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
        text=True,
        encoding='utf-8'
    )
    stdout = result.stdout.strip()
    lines = [l for l in stdout.splitlines()
             if l and not l.startswith('timestamp')]
    if not lines:
        print('no output')
        continue
    row = next(csv.reader([lines[0]]))
    row[0] = timestamp
    row[1] = short_name
    while len(row) < len(header):
        row.append('')
    rows.append(row[:len(header)])
    print('CMI=' + row[2] + '  level=' + row[3])

with open(out_path, 'w', newline='', encoding='utf-8-sig') as f:
    w = csv.writer(f)
    w.writerow(header)
    w.writerows(rows)

print('done: ' + str(len(rows)) + ' files -> ' + out_path)
