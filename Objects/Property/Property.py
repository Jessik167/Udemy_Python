class Product:
    def __init__(self,x,y):
        self._x = x
        self._y = y

    def display(self):
        print(self._x, self._y)

    @property
    def value(self):
        return self._x

    @value.setter
    def value(self, val):
        self._x = val

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, val):
        self._y = val

p = Product(12,24)
print(p.value)
p.value + 2
dir(Product)
p.value = 10
p.value = 20
print(p.y)
p.y = 12
print(p.value)
print(p.y)
print('--------------------')

class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age

    def display(self):
        print(self.name,self._age)
    #####################################

    def set_age(self,new_age):
        if 20 < new_age < 80:
            self._age = new_age
        else:
            raise ValueError("Age must be between 20 and 80")

    def get_age(self):
        return self._age

if __name__ == '__main__':
    p = Person('Raj',30)
    # can't modify the age because of the hidding property
    p.age = 100
    p.display()
    #################

    # when you try to run this part raise an error like is written in set_age
    #p.set_age(100)
    #p.set_age(12)

    #set a new age
    p.set_age(25)
    p.display()
    p.set_age(p.get_age()+1)
    p.display()

    # in this case didn't raise the error because the age is instantiated in __init__
    p1 = Person("dev", 200)
    p1.display()