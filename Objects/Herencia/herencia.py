class Person:
    def __init__(self, name, age, address, phone):
        self.name = name
        self.age = age
        self.address = address
        self.phone = phone

    def greet(self):
        print('Hello i am ', self.name)

    def is_adult(self):
        if self.age > 18:
            return True
        else:
            return False

    def contact_details(self):
        print(self.address, self.phone)

class Employee(Person):
    pass

emp = Employee('Alice',30,'D4, XYZ street, Delhi', '5559998785')
print(emp.age)
emp.greet()
emp.contact_details()
print(emp.is_adult())
print('*'* 10)

print(isinstance(emp,Employee))
print(isinstance(emp,Person))
print(issubclass(Employee,Person))

print('*'* 10)
#In Python everything is a subclass of an object
print(issubclass(Person,object))
print(issubclass(str,object))
print(issubclass(int,object))