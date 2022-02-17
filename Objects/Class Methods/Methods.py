class MyClass:
    a = 5
    def __init__(self, x):
        self._x = x

    def method1(self):
        print(self.x)

    '''The method only can access to class variables'''
    @classmethod
    def method2(cls):
        print(cls.a)


'''Because its a class method and have no relation with the instances it's possible to called it this way.
It could be called as an instance but since is a class method makes more sense this way.'''
MyClass.method2()

