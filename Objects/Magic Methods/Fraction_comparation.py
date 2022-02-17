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

    def __add__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        f = Fraction(self.nr * other.dr + other.nr * self.dr, self.dr * other.dr)
        f._reduce()
        return f

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

#equal method
f1 = Fraction(2,3)
f2 = Fraction(2,3)
f3 = Fraction(4,6)

print(f1 == f2)
print(f1 == f3)
print(f1 != f2)
print('*'*10)

#less method
f1 = Fraction(2,3)
f2 = Fraction(2,3)
f3 = Fraction(1,5)

print(f1 < f2)
print(f1 <= f2)
print(f1 < f3)
print(f3 < f1)


