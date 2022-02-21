class Person:
    def greet(self):
        print("I'm a Person")


class Teacher(Person):
    def greet(self):
        super().greet()
        print("I'm a Teacher")


class Student(Person):
    def greet(self):
        super().greet()
        print("I'm a Student")


class TeachingAssitant(Student, Teacher):
    def greet(self):
        super().greet()
        print("I'm a Teaching Assistant")


TA = TeachingAssitant()
TA.greet()
print()

print(help(TeachingAssitant))