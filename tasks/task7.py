from pathlib import Path

directory = Path(input("Каталог: ").strip())
ext = input("Расширение: ").strip()

if ext[0] != '.':
    ext = "." + ext

try:
    if not directory.is_dir():
        raise FileNotFoundError(directory)
    for path in directory.rglob(f"*{ext}"):
        if path.is_file():
            print(f"{path}  {path.stat().st_size} байт")

except FileNotFoundError:
    print(f"Каталог не существует: {directory}")
except PermissionError:
    print(f"Нет доступа к каталогу: {directory}")