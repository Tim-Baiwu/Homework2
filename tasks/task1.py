
def analyze_text(directory):
    line_count = word_count = char_count = max_line_len = 0
    with open(directory, "r", encoding="utf-8") as f:
        for line in f:
            line_count += 1
            char_count += len(line)
            line = line.rstrip("\n")
            max_line_len = max(max_line_len, len(line))
            word_count += len(line.split())
    return line_count, word_count, char_count, max_line_len

direct = "test.txt"
print(f"Кол-во строк: {analyze_text(direct)[0]}")
print(f"Кол-во слов: {analyze_text(direct)[1]}")
print(f"Кол-во символов: {analyze_text(direct)[2]}")
print(f"Макс. кол-во символов в строке: {analyze_text(direct)[3]}")