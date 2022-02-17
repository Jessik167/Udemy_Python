class Account:
    rate = 5
    def some_method(self):
        print(self.rate, Account.rate, id(self.rate), id(Account.rate))
        self.rate = 10
        print(self.rate, Account.rate, id(self.rate), id(Account.rate))
        Account.rate = 10
        print(self.rate, Account.rate, id(self.rate), id(Account.rate))
        print("---------------------------------------------")

a1 = Account()
a2 = Account()

a1.some_method()