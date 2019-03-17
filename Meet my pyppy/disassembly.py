#!/bin/python3

import dis
import inspect

from array import *


def fib(n):
    if n <= 2:
        return 1
    return fib(n-1) + fib(n-2)


dis.dis(fib)
print(inspect.getfile(fib.__code__))
print(inspect.getdoc(dis))

new_array = array('b', [1, 2, 3, 4, 5])
print(new_array)
print(new_array.reverse())
new_array.append(9)
print(new_array)

extension_array = array('b', [5, 6, 8, 10])
new_array.extend(extension_array)
new_array.remove(5)
new_array.remove(5)
new_array.fromlist([0, 0, 0, -1])
new_array[3] = new_array[0]
print(new_array)
print(new_array.tostring())
print(new_array.tolist())
