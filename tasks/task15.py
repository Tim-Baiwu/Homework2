from io import StringIO

def count_lines(stream):
    return sum(1 for _ in stream)

with open("data.txt", encoding="utf-8") as f:
    print(count_lines(f))

print(count_lines(StringIO("first\nsecond\nthird")))