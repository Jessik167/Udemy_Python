class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
        '''if we do it this way at the time we modify some of the values above diagonal won't change. 
        This is because we are setting this calculation on __init__'''
        #self.diagonal = (self.length * self.length + self.breadth * self.breadth) ** 0.5

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2*(self.length + self.breadth)

    '''On the other hand, doing diagonal this way we assure that if we change some attribute value,
    the calculation will be different'''
    @property
    def diagonal(self):
        return (self.length * self.length + self.breadth * self.breadth) ** 0.5


r = Rectangle(2,5)
print(r.diagonal)
print(r.area())
print(r.perimeter())
print("---------------")

r.length = 10
print(r.diagonal)
print(r.area())
print(r.perimeter())
