import decimal

class BankAccount:
    def __init__(self, int_rate, balance=0):
        self.int_rate = int_rate
        self.balance =  balance


    def deposit(self, amount):
        self.balance += amount
        print(f"Your new balance is {self.balance}")
        return self

    def withdraw(self, amount):
        if self.balance < amount:
            print(f"Insuficient funds. Charging a $5 fee.")
            self.balance -= 5
        else:
            self.balance -= amount
            print(f"You've withdrawn: ${amount}. You're new balance is: ${self.balance}")
        return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        return self
    
    def transfer_money(self, amount, receiver):
        self.balance -= amount
        receiver.balance += amount
        return self


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance = 0)

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self

    def display_user_balance(self):
        self.account.display_account_info()
        return self

    def transfer(self, amount, receiver):
        self.make_withdrawal(amount)
        receiver.make_deposit(amount)
        return self



ivan = User("Ivan", "email@email.com")
rem = User("Rem", "remita@email.com")

ivan.make_deposit(100).transfer(55, rem).display_user_balance()
rem.transfer(10, ivan).display_user_balance()

