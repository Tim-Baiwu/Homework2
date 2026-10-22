from contextlib import contextmanager

@contextmanager
def log_operation(filename, name):
    with open(filename, "a", encoding="utf-8") as log:
        log.write(f"START: {name}\n")
        try:
            yield
        except Exception:
            log.write(f"ERROR: {name}\n")
            raise
        else:
            log.write(f"END: {name}\n")
