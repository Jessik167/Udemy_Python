class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("I am ", self.name)

    def greet(self):
        if self.age > 80:
            print("Hi, How are you doing ?")
        else:
            print("Hello, How do you d o ?")
        self.display()

p1 = Person("Bob", 30)
p1.greet()
p2 = Person("Ted", 90)
p2.greet()


class Test:
    pass


t1 = Test()
t2 = Test()
print(t1 == t2, end=' ')
print(type(t1) == type(t2), end=' ')