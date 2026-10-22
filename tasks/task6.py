from pathlib import Path

root = Path(input("Каталог: "))

files = [p for p in root.rglob("*") if p.is_file()]
dirs = [p for p in root.rglob("*") if p.is_dir()]
py_files = [p for p in files if p.suffix == ".py"]
total_size = sum(p.stat().st_size for p in files)

print(f"Файлов: {len(files)}")
print(f"Подкаталогов: {len(dirs)}")
print("Python-файлы:")
for p in py_files:
    print(" ", p)
print(f"Суммарный размер: {total_size} байт")