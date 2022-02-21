class Person:
    def greet(self):
        print("I'm a Person")


class Teacher(Person):
    def greet(self):
        print("I'm a Teacher")


class Student(Person):
    def greet(self):
        print("I'm a Student")


class TeachingAssitant(Student, Teacher):
    def greet(self):
        print("I'm a Teaching Assistant")


TA = TeachingAssitant()
TA.greet()

# This shows the order of inheritance
print(help(TeachingAssitant))

# This shows the order in a tuple
print(TeachingAssitant.__mro__)

# This shows the order in a list
print(TeachingAssitant.mro())