import re
from collections import Counter

LINE_RE = re.compile(
    r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} "
    r"(?P<level>INFO|WARNING|ERROR) User (?P<user>\d+)"
)

levels = Counter()
error_users = set()

with open("big.log", encoding="utf-8") as f:
    for line in f:
        m = LINE_RE.match(line)
        if not m:
            continue
        levels[m["level"]] += 1
        if m["level"] == "ERROR":
            error_users.add(m["user"])

for level in ("INFO", "WARNING", "ERROR"):
    print(f"{level}: {levels[level]}")

print("Пользователи с ошибками:", sorted(error_users, key=int))