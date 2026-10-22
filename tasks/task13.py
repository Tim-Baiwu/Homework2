import time

class Timer:
    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc, tb):
        self.elapsed = time.perf_counter() - self.start
        print(f"Время выполнения: {self.elapsed:.4f} с")
        return False

# from contextlib import contextmanager
#
# @contextmanager
# def Timer():
#     start = time.perf_counter()
#     try:
#         yield
#     finally:
#         print(f"Время выполнения: {time.perf_counter() - start:.4f} с")

def f(n):
    print([i**2 for i in range(n)])

with Timer():
    f(100000)