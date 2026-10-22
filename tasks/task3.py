import csv
students = []
with open("students.csv", encoding="utf-8") as file:
    f = csv.DictReader(file)
    for row in f:
        students.append({
            "name": row["name"],
            "group": row["group"],
            "score": int(row["score"])
        })

av = (sum(student["score"] for student in students) / len(students))
print("Средний балл:", av)
best_student = max(students, key=lambda student: student["score"])
print("Лучший студент:", best_student["name"], best_student["score"])

groups = {}
for student in students:
    group = student["group"]
    if group not in groups:
        groups[group] = []
    groups[group].append(student["score"])

print("Средний балл групп:")

for group, scores in groups.items():
    average_group = sum(scores) / len(scores)
    print(group, average_group)