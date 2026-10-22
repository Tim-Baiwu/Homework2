import re

text = """Контакты:
alice@example.com
bob@test.org
alice@example.com
admin@company.ru"""

emails = re.findall(r"[\w.+]+@[\w]+(?:\.[\w]+)+", text)
for email in dict.fromkeys(emails):
    print(email)