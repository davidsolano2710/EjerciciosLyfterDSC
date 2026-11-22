class BankAccount:
    def __init__(self):
        self.balance = 0


    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")


    def withdraw(self, amount):
        if amount < 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew: {amount}. New balance: {self.balance}")


class SavingsAccount(BankAccount):
    def __init__(self, mim_balance):
        super().__init__()                #super() is used to use the methods of the parent class, in this case, the BankAccount class.
        self.min_balance = mim_balance

    def withdraw(self, amount):
        if self.balance - amount < self.min_balance:
            print("Cannot withdraw. Minimum balance requirement not met.")
        else:
            super().withdraw(amount)


savings_account = SavingsAccount(100)
savings_account.deposit(200)
print(f"Current balance: {savings_account.balance}")
savings_account.withdraw(50)
print(f"Current balance: {savings_account.balance}")
savings_account.withdraw(1000)
