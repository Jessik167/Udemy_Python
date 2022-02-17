class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self._radius * self._radius

    def display(self):
        print("-" * 50)
        print(self.radius,self.diameter, self.circumference)

    @property
    def diameter(self):
        return 2 * self._radius

    @property
    def circumference(self):
        return 2*3.14*self._radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, val):
        if val > 0:
            self._radius = val
        else:
            raise ValueError("The value must be an non-negative number.")


c = Circle(7)
c.display()
print("Area:", c.area())

c.radius = 10
c.display()

#c.radius = -1