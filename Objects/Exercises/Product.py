class Product():
    def __init__(self, id, marked_price, discount):
        self.id = id
        self.marked_price = marked_price
        self._discount = discount

    def display(self):
        print(self.id, self.marked_price, self.discount)

    @property
    def selling_price(self):
        return self.marked_price * (1-self.discount/100)

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self,new_discount):
        if self.marked_price > 500:
            self._discount += new_discount
        else:
            print("The price must be above 500")
            print("---------------------------")


p1 = Product('X879', 400, 6)
p2 = Product('A234', 100, 5)
p3 = Product('B987', 990, 4)
p4 = Product('H456', 800, 6)

p1.discount = 2
p3.discount = 10

p1.display()
print("discount price: ",p1.selling_price)

p2.display()
print("discount price: ",p2.selling_price)

p3.display()
print("discount price: ",p3.selling_price)

p4.display()
print("discount price: ",p4.selling_price)
