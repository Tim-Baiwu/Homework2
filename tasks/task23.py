import re

text = "Это   строка    с     большим    количеством   пробелов."
print(re.sub(r" {2,}", " ", text))

text2 = "   Текст   с   пробелами   "
print(re.sub(r"\s+", " ", text2).strip())
