def addition(a,b,c):
    return a+b+c


def substraction(a,b,d):
    return a-b-d


def divison(a,b,c):
    return a/b/c


class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds!")

    def get_balance(self):
        return self.balance


account = BankAccount()
account.deposit(100)
account.withdraw(30)
print(account.get_balance())  # Output: 70
