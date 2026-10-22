import re

text = "Звоните +7 999 123-45-67, 8 999 123-45-67, +7 (999) 123-45-67 или 8 (999) 123-45-67."
pattern = r"(?:\+7|8)\s(?:\(\d{3}\)|\d{3})\s\d{3}-\d{2}-\d{2}"

for phone in re.findall(pattern, text):
    print(phone)