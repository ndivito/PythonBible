class Account:
    def __init__(self, name, balance, min_balance):
        self.name = name
        self.balance = balance
        self.min_balance = min_balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance - amount >= self.min_balance:
            self.balance -= amount
        else:
            print("Sorry, not enough funds.")

    def statement(self):
        print("Account balance: ${}".format(self.balance))



class Current(Account):
    def __init__(self, name, balance):
        super().__init__(name, balance, min_balance=-1000)

    def __str__(self):
        return "{}'s Current Account : Balance ${}".format(self.name, self.balance)


class Savings(Account):
    def __init__(self, name, balance):
        super().__init__(name, balance, min_balance=0)

    def __str__(self):
        return "{}'s Savings Account : Balance ${}".format(self.name, self.balance)

x = Current("Nick", 9999999)
x.deposit(800)
x.statement()
x.withdraw(45682)
x.statement()
print(x)

xx = Current("Nick", 800)
xx.deposit(800)
xx.statement()
xx.withdraw(45682)
xx.withdraw(482)
xx.statement()
print(xx)