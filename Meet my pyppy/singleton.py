

class Singleton:
    number = 0
    random = 0

    def __new__(cls):                               # provides only one instantiation of class
        try:
            it = cls.__it__                         # class attribute
        except AttributeError:
            it = cls.__it__ = object.__new__(cls)   # use object's constructor to instantiate object of singleton class
            cls.number = cls.number + 1             # used to check if it actually is made only once xd
        return it

    def __repr__(self):
        return f"<{self.__class__.__name__.upper()}>"

    def __eq__(self, other):
        return other is self

    def class_attr(self):
        if self.random is not 1:
            self.random += 1
        else:
            pass


s = Singleton()
s.class_attr()
print(s.__repr__() + f' {s.number}, random = {s.random}')

s2 = Singleton()
s2.class_attr()
print(s.__repr__() + f' {s2.number}, random = {s2.random}')

s3 = Singleton()
s3.class_attr()
print(str(s) + f' {s3.number}, random = {s3.random}')
