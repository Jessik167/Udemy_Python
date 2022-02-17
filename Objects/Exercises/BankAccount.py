class BankAccount:
    def set_details(self, name, balance=0):
        self.name = name
        self.balance = balance

    def display(self):
        print(f"Hello {self.name}, your balance is ${self.balance}")
        print("------------------------------")

    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

p1 = BankAccount()
p2 = BankAccount()

p1.set_details("Alice", 200)
p2.set_details("Robert")

p1.display()
p2.display()

p1.deposit(50)
p2.deposit(100)

p1.display()
p2.display()

p1.withdraw(40)
p2.withdraw(50)

p1.display()
p2.display()

