class BankAccount:
    def __init__(self, account_holder, balance=float(0)):
        self.account_holder = account_holder
        self.balance = balance

    def withdraw(self, draw_amount):
        if self.balance >= draw_amount:
            self.balance -= draw_amount
            print(f"You withdrew ${draw_amount:.2f}. You have ${self.balance:.2f} remaining.")
        else:
            print("Insufficient funds!")

    def deposit(self, dep_amount):
        self.balance += dep_amount
        print(f"You deposited ${dep_amount:.2f}. You have ${self.balance:.2f} in the bank.")

    def show_balance(self):
        return self.balance
