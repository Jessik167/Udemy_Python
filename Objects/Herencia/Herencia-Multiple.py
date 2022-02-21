class Teacher:
    def greet(self):
        print("Hi, i'm a teacher")

class Student:
    def greet(self):
        print("Hi, i'm a student")

class TeachingAssistant(Student,Teacher):
    pass
    '''
    def greet(self):
        print("Hi, i'm a Teaching Assistant")
    '''


TA = TeachingAssistant()
'''Calling greet method will call the one in the TeachingAssitant class, but if we delete this method
the one that will call would be according to its inheritance, in this case will call the method in Student
class. If we change the order this will change too.'''
TA.greet()