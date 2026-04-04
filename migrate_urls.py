import os

urls_file = 'D:/r8_strategy/urls.txt'
todo_file = 'D:/r8_strategy/urls_todo.txt'

with open(urls_file, 'r', encoding='utf-8') as f:
    lines = f.readlines()

urls = [l.strip() for l in lines if l.strip() and not l.startswith('#')]

start_num = 65
entries = []
for i, url in enumerate(urls):
    file_id = f"AD_{start_num + i:03d}_20260404"
    entries.append(f"{url}\t{file_id}\n")

with open(todo_file, 'a', encoding='utf-8') as f:
    f.writelines(entries)

print(f"{len(entries)}件を追記しました")
for e in entries:
    print(e.strip())
