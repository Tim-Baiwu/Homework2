import json
import logging
import re
from collections import Counter

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
)
log = logging.getLogger(__name__)

LINE_RE = re.compile(
    r"^(?P<date>\S+) (?P<time>\S+) "
    r"(?P<ip>\d{1,3}(?:\.\d{1,3}){3}) "
    r"(?P<method>[A-Z]+) (?P<url>\S+) (?P<status>\d{3})$"
)

def process(path="access.log", out="stats.json"):
    methods = Counter()
    urls = Counter()
    errors_4xx = 0
    skipped = 0
    try:
        with open(path, encoding="utf-8") as f:
            log.info(f"Начинаю обработку {path}")
            for linenumb, line in enumerate(f, start=1):
                m = LINE_RE.match(line.strip())
                if not m:
                    skipped += 1
                    log.warning(f"Строка {linenumb} не распознана: {line.strip()}")
                    continue
                methods[m["method"]] += 1
                urls[m["url"]] += 1
                if m["status"][0] == "4":
                    errors_4xx += 1
    except FileNotFoundError:
        log.error(f"Файл не найден: {path}")
        return
    except PermissionError:
        log.error(f"Нет прав доступа: {path}")
        return
    except UnicodeDecodeError:
        log.error(f"Не удалось декодировать файл: {path}")
        return
    except OSError as e:
        log.error(f"Ошибка чтения файла: {e}")
        return

    result = {
        "requests_by_method": dict(methods),
        "errors_4xx": errors_4xx,
        "most_common_url": urls.most_common(1)[0][0] if urls else None,
        "skipped_lines": skipped,
    }

    with open(out, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=4)
    log.info(f"Статистика сохранена в {out}")

process()