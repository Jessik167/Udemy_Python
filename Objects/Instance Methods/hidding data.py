class Product:

    def __init__(self):
        self.data1 = 10
        self.__data2 = 20

    def methodA(self):
        pass

    def __methodB(self):
        pass

p = Product()
# We can't access to data this way
#p.__data2
#p.__methodB()

# But we can this way
print(p._Product__data2)
p._Product__methodB()