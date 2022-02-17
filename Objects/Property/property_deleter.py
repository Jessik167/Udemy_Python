class Product:
    def __init__(self,x,y):
        self._x = x
        self._y = y

    def display(self):
        try:
            print(self._x,self._y)
        except AttributeError:
            print("You have to set to 'x' or 'y' some value")

    @property
    def value(self):
        return self._x

    @value.setter
    def value(self, val):
        self._x = val

    @value.deleter
    def value(self):
        print("Value deleted..")
        del self._x

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self,val):
        self._y = val

p = Product(12,24)
p.display()
del p.value
p.display()
p.value = 10
p.display()

