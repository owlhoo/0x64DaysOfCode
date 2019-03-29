from functools import lru_cache


# expensive functions wrapper, lru algorithm to save already computed stuff
@lru_cache(maxsize=None)
def fib(x): return 1 if x == 0 or x == 1 else fib(x - 1) + fib(x - 2)


def init_dict(dicting, index):
    array = list(dicting.keys())
    start = 0 if not array else array[-1]

    for i in range(start, index + 1):
        dicting[i] = fib(i)


def get_fibonacci(fibonacci, index):
    while True:
        if fibonacci.get(index) is not None:
            print(fibonacci[index])
            break
        else:
            init_dict(fibonacci, index)


fibonacci_array = {}

init_dict(dicting=fibonacci_array, index=int(input('Enter initialisation upper bound: ')))

while True:
    get_fibonacci(fibonacci_array, int(input('Enter the index of wanted element in array: ')))
