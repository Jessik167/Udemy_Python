class Acount:
    rate = 5

a1 = Acount()
a2 = Acount()

print(Acount.rate)
print(a1.rate)
print(a2.rate)
print("------------")

Acount.rate = 6
print(Acount.rate)
print(a1.rate)
print(a2.rate)
print("------------")

a1.rate = 7
print(Acount.rate)
print(a1.rate)
print(a2.rate)
print("------------")

print(id(Acount.rate))
print(id(a1.rate))
print(id(a2.rate))