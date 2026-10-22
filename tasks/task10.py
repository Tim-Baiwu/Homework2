class BankError(Exception):
    pass

class InvalidAmountError(BankError):
    pass

class InsufficientFundsError(BankError):
    pass

class AccountBlockedError(BankError):
    pass

def withdraw(balance, amount):
    if amount <= 0:
        raise InvalidAmountError(f"Некорректная сумма: {amount}")
    if amount > balance:
        raise InsufficientFundsError(f"Недостаточно средств: {balance} < {amount}")
    return balance - amount

try:
    print(withdraw(100, 30))
    print(withdraw(70, 100))
except BankError as e:
    print("Ошибка:", e)