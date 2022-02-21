import math

class Rectangle:
    name = 'Rectangle'
    def __init__(self,length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)

class Triangle:
    name = 'Triangle'
    def __init__(self, s1, s2, s3):
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3

    def area(self):
        sp = (self.s1 + self.s2 + self.s3) / 2
        return math.sqrt(sp * (sp - self.s1) * (sp - self.s2) * (sp - self.s3))

    def perimeter(self):
        return self.s1 + self.s2 + self.s3


class Circle:
    name = 'Circle'
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return 3.1416 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.1416 * self.radius

r1 = Rectangle(13,25)
r2 = Rectangle(14,16)
t1 = Triangle(14,17,12)
t2 = Triangle(25,33,52)
c1 = Circle(14)
c2 = Circle(25)

def find_area_perimeter(shape):
    print(shape.name)
    print('Area: ', shape.area())
    print('Perimeter: ', shape.perimeter())
    print('*'*20)

find_area_perimeter(t2)
find_area_perimeter(c1)
find_area_perimeter(r2)

'''We want to calculate the total area and perimeter of each object'''
shapes = [r1,r2,t1,t2,c1,c2]

total_area = 0
total_perimeter = 0

for shape in shapes:
    total_area += shape.area()
    total_perimeter += shape.perimeter()

print('Total Area: ', total_area)
print('Total Perimeter: ', total_perimeter)