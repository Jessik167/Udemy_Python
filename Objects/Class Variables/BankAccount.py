class BankAccount:
    rate_of_interest = 5
    min_balance = 100
    min_balance_fees = 10

    def __init__(self, account_number, owner_name, balance):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance

    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

account1 = BankAccount('7248', 'Tom', 50)
account2 = BankAccount('6378', 'Bob', 400)

account1.deposit(70)
print(account1.balance)
account2.withdraw(50)
print(account2.balance)
print(BankAccount.min_balance)