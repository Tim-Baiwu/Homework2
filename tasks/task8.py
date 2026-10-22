def read_file(path):
    try:
        with open(path, encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"Файл не найден: {path}")
    except PermissionError:
        print(f"Нет прав доступа к файлу: {path}")
    except IsADirectoryError:
        print(f"Это каталог, а не файл: {path}")
    except UnicodeDecodeError:
        print(f"Файл невозможно прочитать как текст UTF-8: {path}")
    except OSError as e:
        print(f"Ошибка операционной системы: {e}")
    return None

read_file("resultf.txt")