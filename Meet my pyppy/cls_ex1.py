# the polite way of enforcing abstraction


class Fruit:

    def check_is_delicious(self):
        raise NotImplementedError("can't be delicious if not implemented..")


class Pear(Fruit):

    def check_is_delicious(self):
        print('I AM DELICIOUS')


a = Pear()
a.check_is_delicious()


# the not so polite way

from abc import ABCMeta, abstractmethod


class MyAbstractClass(object):
    # this is a must, always has to be a class variable
    __metaclass__ = ABCMeta

    # decorator tells that this method is undefined
    @abstractmethod
    def children_must_define_me(self):
        # can be left blank or a base implementation
        return None


class ChildClass(MyAbstractClass):

    def children_must_define_me(self):
        print('I AM DEFINED FINALLY')
        print(super(ChildClass, self).children_must_define_me())
        return


print(MyAbstractClass().children_must_define_me())
print(ChildClass().children_must_define_me())
