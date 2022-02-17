class Person:
    species = 'Homo sapiens'
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"{self.name} is {self.age} years old")

p1 = Person("John", 20)
p2 = Person("Jack", 34)
p1.display()
p2.display()
print(Person.species)
print(p1.species)
print(p2.species)
#print(Person.name)

print(id(p1.species))
print(id(p1.name))

print(id(p2.species))
print(id(p2.name))
#d(Person.species)
#print(f"{self.name} is {self.age} years old {Person.species}")

