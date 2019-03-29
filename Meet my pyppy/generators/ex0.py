import sys


def accumulator():
    total = 0
    value = None

    while True:
        value = yield total

        if value is None:
            break

        total += value


generator = accumulator()

# advances to the first yield
next(generator)

# aggregating values
print(generator.send(2))
print(generator.send(20))
print(generator.send(200))
print(generator.send(2000))
print(generator.send(20000))
print(generator.send(200000))
print(generator.send(2000000))

# generator.send(None) - stopping the generator
# next(generator)              raises StopIteration


generator = (i * 2 for i in range(3))

print(next(generator))
print(next(generator))
print(next(generator))
# print(next(generator))       4th one raises StopIteration

# del generator

print(sys.getrefcount(generator))

# parenthesis from the function call makes the expression generator expression implicitly
print(sum(i ** 2 for i in range(4)))
