
def reading_file(directory):
    numbers = anomalies = []
    with open(directory, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                numbers.append(int(line))
            except ValueError:
                anomalies.append(line)
    return numbers, anomalies

def write_result(directory, numbers):
    with open(directory, "w", encoding="utf-8") as f:
        if numbers:
            f.write(f"Кол-во чисел: {len(numbers)}\n")
            f.write(f"Минимум: {min(numbers)}\n")
            f.write(f"Максимум: {max(numbers)}\n")
            f.write(f"Среднее арифметическое: {(sum(numbers)/len(numbers)):.2f}\n")
        else:
            f.write("Не удалось считать файл, в нем нет корректных чисел.\n")

numb_direct = "numbers.txt"
result_direct = "result.txt"
numbers = reading_file(numb_direct)[0]
write_result(result_direct, numbers)




