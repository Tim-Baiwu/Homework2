def stats(path):
    total = count = 0
    minimum = maximum = None
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            n = int(line)
            total += n
            count += 1
            minimum = n if minimum is None else min(minimum, n)
            maximum = n if maximum is None else max(maximum, n)
    return total, count, minimum, maximum


total, count, mn, mx = stats("huge_numbers.txt")
if count:
    print(f"Сумма: {total}\nМинимум: {mn}\nМаксимум: {mx}")
    print(f"Количество: {count}\nСреднее: {total / count:.2f}")