class Fraction:
    def __init__(self, nr, dr=1):
        self.nr = nr
        self.dr = abs(dr)
        if self.dr < 0:
            self.nr *= -1
            self.dr *= -1
        self._reduce()

    def show(self):
        print(f"{self.nr}/{self.dr}")

    def __str__(self):
        return f"{self.nr}/{self.dr}"

    # This is for console interative print
    def __repr__(self):
        return f"Fraction({self.nr},{self.dr})"

    def __add__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        f = Fraction(self.nr * other.dr + other.nr * self.dr, self.dr * other.dr)
        f._reduce()
        return f

    #Reverse add method
    '''When Python calls the dunder reverse add method on the instance object f and passes 3 as
    the parameter to this method'''
    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        f = Fraction(self.nr * other.dr - other.nr * self.dr, self.dr * other.dr)
        f._reduce()
        return f

    def __mul__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        f = Fraction(self.nr * other.nr , self.dr * other.dr)
        f._reduce()
        return f

    def __eq__(self, other):
        return (self.nr * other.dr) == (self.dr * other.nr)

    def __lt__(self, other):
        return (self.nr * other.dr) < (self.dr * other.nr)

    def __le__(self, other):
        return (self.nr * other.dr) <= (self.dr * other.nr)

    def _reduce(self):
        h = Fraction.hcf(self.nr, self.dr)
        if h == 0:
            return

        self.nr //= h
        self.dr //= h

    @staticmethod
    def hcf(x, y):
        x = abs(x)
        y = abs(y)
        smaller = y if x > y else x
        s = smaller
        while s > 0:
            if x % s == 0 and y % s == 0:
                break
            s -= 1
        return s


'''This works because the 'dunder' add method its design to receive an int as parameter'''
f = Fraction(2,3)
f2 = f + 3
print(f2)

'''This raise an error because in the left opperator is an integer and int class does not have
a dunder add method that can add our Fraction type.

In this case Python will look for a dunder reverse add method that supports an int.

Once we have a reverse add method this works.'''
f2 = 3 + f
print(f2)


