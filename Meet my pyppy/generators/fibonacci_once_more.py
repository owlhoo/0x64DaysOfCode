import time
from functools import lru_cache


def fib(a=0, b=1):
    while True:
        yield a
        a, b = b, a + b


def fib_list(a=0, b=1, index=0):
    result = [a, b]
    i = 1
    while i < index:
        result.append(result[i-2] + result[i-1])
        i += 1
    return result[index-1]


@lru_cache(maxsize=None)
def fib_recursive(x): return 1 if x == 0 or x == 1 else fib_recursive(x - 1) + fib_recursive(x - 2)


def fib_through_recursive(x):
    yield from fib_recursive(x)


print('Generator fibonacci fun started.')
t0_gen = time.time()
((next(fib())) for _ in range(100000))
t1_gen = time.time()
print(f'Generator fibonacci fun took {t1_gen - t0_gen} secs')

print('List fun started.')
t0_gen = time.time()
fib_list(index=100000)
t1_gen = time.time()
print(f'List fibonacci fun took {t1_gen - t0_gen} secs')

print('Recursive fibonacci fun started.')
t0_gen = time.time()
fib_through_recursive(100000)
t1_gen = time.time()
print(f'Recursive fibonacci fun took {t1_gen - t0_gen} secs')
