class Employee:
    def __init__(self, name, password, salary):
        self._name = name
        self._password = password
        self._salary = salary

    def display_user(self):
        print("---------")
        print(self._name, self._salary)

    '''When we only assing property and not a setter this method become in *read only*'''
    @property
    def name(self):
        return self._name

    '''On Password method is *write only* because we have raised this AttributeError'''
    @property
    def password(self):
        raise AttributeError("password not readable")

    @password.setter
    def password(self, new_password):
        self._password = new_password

    '''When we provide both getter and setter methods, the property becomes *read/write*'''
    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, new_salary):
        self._salary = new_salary


e = Employee("Jill",'Feb31', 5000)
print(e.name)
#e.name = 'dd'
#print(e.password)
e.password = 'Feb29'
print(e.salary)
e.salary = 6000
e.display_user()
