import re

path = r"D:\r8_strategy\ailabel\ailabel_claude.py"

with open(path, encoding="utf-8") as f:
    text = f.read()

# JSON出力形式の波括弧をエスケープ（format()対応）
old = '''{
  "label": "HIGH/MEDIUM/LOW/Intent-Unresolved",
  "primary_condition": "H-1/H-2/H-3/H-4/M-1/M-2/M-3/M-4/L-1/L-2/L-3/IU",
  "confidence": "high/medium/low",
  "reason": "判定根拠を1〜2文で"
}'''

new = '''{{
  "label": "HIGH/MEDIUM/LOW/Intent-Unresolved",
  "primary_condition": "H-1/H-2/H-3/H-4/M-1/M-2/M-3/M-4/L-1/L-2/L-3/IU",
  "confidence": "high/medium/low",
  "reason": "判定根拠を1〜2文で"
}}'''

if old in text:
    text = text.replace(old, new)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    print("修正完了: JSON波括弧をエスケープしました")
else:
    print("対象文字列が見つかりません — 既に修正済みか確認してください")
    # 現状のJSON部分を表示
    idx = text.find('"label"')
    if idx > 0:
        print("現状:", repr(text[idx-5:idx+20]))
