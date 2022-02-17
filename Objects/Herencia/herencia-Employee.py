class Person:
    def __init__(self, name, age, address, phone):
        self.name = name
        self.age = age
        self.address = address
        self.phone = phone

    def greet(self):
        print('Hello i am ', self.name)

    def is_adult(self):
        if self.age > 18:
            return True
        else:
            return False

    def contact_details(self):
        print(self.address, self.phone)


class Employee(Person):
    def __init__(self, name, age, address, phone, salary, office_address, office_phone):
        '''We can copy the code like in the base class, but this can be repetitive and difficult to mantain'''
        #self.name = name
        #self.age = age
        #self.address = address
        #self.phone = phone
        '''Insted we use the class'''
        #Person.__init__(self,name,age,address,phone)
        '''But the correct way to call the base class it's super, and we can forget about self'''
        super().__init__(name,age,address,phone)
        #New instances for Employee
        self.salary = salary
        self.office_address = office_address
        self.office_phone = office_phone

    '''When create an method with the same name as the base class this overrates this and hide the one
    in the base class.
    On this method it's possible to modify it, we can write a complete new method corresponding to this class
    (Employee) or we can add new functionalities besides the base class'''
    def contact_details(self):
        '''Code from base class'''
        #print(self.address, self.phone)
        '''calling super class'''
        super().contact_details()
        print(self.office_address,self.office_phone)

    def calculate_tax(self):
        if self.salary < 5000:
            return 0
        else:
            return self.salary * 0.05


emp = Employee('Alice',30,'D4, XYZ street, Delhi', '5559998785', 8000, 'ABC street, CDMX','5548692615')
print(emp.salary)
print(emp.calculate_tax())
emp.contact_details()