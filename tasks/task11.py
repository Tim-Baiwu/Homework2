import re

with open("app.log", encoding="utf-8") as f:
    text = f.read()

user_ids = re.findall(r"User (\d+)", text)
error_lines = re.findall(r"^ERROR.*$", text, flags=re.MULTILINE)
error_users = sorted(set(re.findall(r"^ERROR User (\d+)", text, flags=re.MULTILINE)))

print("Все пользователи:", user_ids)
print("Строки ERROR:", error_lines)
print("Пользователи с ошибками:", error_users)