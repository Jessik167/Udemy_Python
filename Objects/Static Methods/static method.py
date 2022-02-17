class MyClass:
    a = 5

    def __init__(self,x):
        self.x = x

    #instance method: access only to instance variables
    def method1(self):
        print(self.x)

    #Class method: access only to class variables and has the availity to be a factory method
    @classmethod
    def method2(cls):
        print(cls.a)

    '''
    * static method doesn't have an special parameter like the other methods. 
    * This method can't access to instance object state or class state.
    
    This method is useful when we have to create a helper or a utility method, that contains some logic
    related to the class'''
    @staticmethod
    def method3(m,n):
        return m + n

