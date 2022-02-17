# name of file , name of class
from Employee import Employee
#
from datetime import datetime

class Person:
    species = 'Homo sapiens'
    count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.count += 1

    def display(self):
        print(f"{self.name} is {self.age} years old")

    '''This methods are called factory methods, which create instance object in different types of data.
    We cannot have more than one definitions for __init__ method inside a class'''
    @classmethod
    def from_str(cls,s):
        name,age = s.split(',')
        return cls(name,int(age))

    @classmethod
    def from_dict(cls,d):
        return cls(d["name"],d["age"])

    @classmethod
    def from_employee(cls, emp):
        name = emp.first_name + ' ' + emp.last_name
        age = datetime.today().year - emp.birth_year
        return cls(name,age)


p1 = Person('John',20)
p2 = Person('Jack',34)

s = 'Jim, 23'
p3 = Person.from_str(s)
p3.display()

d = {"name": "Jane", "age": 34}
p4 = Person.from_dict(d)
p4.display()

e1 = Employee("James", "Smith", 1990, 6000)
p5 = Person.from_employee(e1)
p5.display()
e1.show()