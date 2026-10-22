import json

with open("students.json", encoding="utf-8") as f:
    students = json.load(f)

for student in students:
    student["passed"] = student["score"] >= 60

best = max(students, key=lambda s: s["score"])
print(f"Максимальный балл: {best['name']} ({best['score']})")

with open("students_updated.json", "w", encoding="utf-8") as f:
    json.dump(students, f, ensure_ascii=False, indent=4)