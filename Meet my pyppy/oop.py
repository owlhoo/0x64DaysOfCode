from abc import abstractmethod, ABCMeta
from types import FunctionType

class RandomAbstractClass(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def multiply(self, other):
        pass

    @abstractmethod
    def __add__(self, other):
        pass


class RandomDerivedClass(RandomAbstractClass):
    x = 3

    def __init__(self, value=None):               # could've used args, kwargs
        if value is not None:
            self.x = value

    @classmethod
    def printme(cls):
        print(getattr(cls, "__str__"))

    def __add__(self, other):
        new = self.x + other.x + 100
        return RandomDerivedClass(new)

    @property
    def my_value(self):
        return self.x

    @my_value.setter
    def my_value(self, value):
        self.x = value

    def __str__(self):
        return f'my value x is {self.x}'


def main():
    rnd = RandomDerivedClass()
    rnd0 = RandomDerivedClass()
    RandomDerivedClass.printme()

    rnd0.my_value = 3
    rnd.my_value = 2
    print(rnd0)
    print(rnd)

    rnd0.x = 5
    print(rnd0.x)
    print(rnd.x)

    rnd_sum = rnd0 + rnd
    print(rnd_sum)


if __name__ == '__main__':
    main()
