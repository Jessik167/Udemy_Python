class Fraction:
    def __init__(self, nr, dr = 1):
        self.nr = nr
        self.dr = abs(dr)

    def show(self):
        print(f"{self.nr}/{self.dr}")

    '''
    My solution
    
    def verify_type(self,frac):
        if type(frac) != Fraction:
            frac = Fraction(frac, 1)
        else:
            frac = Fraction(frac.nr, frac.dr)
        return frac

    def multiply(self, frac):
        frac= self.verify_type(frac)
        frac.nr = self.nr*frac.nr
        frac.dr = self.dr*frac.dr
        return frac

    def add(self,frac):
        frac = self.verify_type(frac)
        frac.nr = self.nr*frac.dr + frac.nr*self.dr
        frac.dr = self.dr*frac.dr
        return frac'''

    '''Teacher solution'''
    def multiply(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        return Fraction(self.nr * other.nr, self.dr * other.dr)

    def add(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        return Fraction(self.nr * other.dr + other.nr * self.dr, self.dr * other.dr)


f1 = Fraction(2,3)
f1.show()
f2 = Fraction(3,4)
f2.show()
f3 = f1.multiply(f2)
f3.show()
f3 = f1.add(f2)
f3.show()
f3 = f1.add(5)
f3.show()
f3 = f1.multiply(5)
f3.show()