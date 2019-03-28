from functools import reduce

lam = lambda x: x*x

print(lam(2))


def printme(fun, *args):
    print('in function lambda: ' + str(fun(*args)))


printme(lambda x: x**2, 2)

listica = (-1, 0, 1, 2, 3, 4, 5 , 6, 7, 8)

parna_listica = list(filter(lambda x: x % 2 == 0, listica))

print(tuple(map(lambda x: x**2, parna_listica)))

# reduce returns a value created by applying function on a iterable object

print(reduce(lambda a, x: a + x, parna_listica))

greeting = lambda x, *args, **kwargs: print(f'Hello {x}, additional arguments are {args, kwargs}')

greeting('John', 'non-kwarg', kwarg=' kwarg')


def kek(numero):
    numero[0] = 51
    numero = [0, 0, 0]


y = [5, 3, 2]
kek(y)
print(y)


