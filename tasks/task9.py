def parse_number(value):
    try:
        return int(value)
    except ValueError:
        return float(value)

for text in ["42", "52.42", "abc"]:
    try:
        print(text, "-", parse_number(text))
    except ValueError:
        print(f"{text}: некорректное число")