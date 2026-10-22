import re

def is_valid_login(login):
    return re.fullmatch(r"[A-Za-z][A-Za-z0-9_]{3,15}", login) is not None

print(is_valid_login("F23424_"))