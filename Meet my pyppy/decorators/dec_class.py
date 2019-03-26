import time


class Decorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print('Before the fun call')
        res = self.func(*args, **kwargs)
        print('After fun call')
        return res

# decorator factory


def decoratorfactory(message):
    def decorator(func):
        def wrapped_fun(*args, **kwargs):                       # takes arguments which are needed for decorator func
            print(f'The decorator factory message: {message}')
            return func(*args, **kwargs)
        return wrapped_fun
    return decorator


@Decorator
def test_fun():
    print('Inside the fun')


@decoratorfactory('I am the message')
def test_fun_2():
    print('Test fun 2')


# singleton decorator


def singleton(cls):
    instance = [None]

    def wrapper(*args, **kwargs):
        if instance[0] is None:
            instance[0] = cls(*args, **kwargs)
            print('I decorated the function for you <3')
        return instance[0]
    return wrapper


@singleton
class SingletonClass:
    instances = 0

    def __init__(self):
        print(f'Instanced singleton {self.instances} time')
        self.instances += 1


def timer(funct):
    def inner_fun(*args, **kwargs):
        t0 = time.time()
        f = funct(*args, **kwargs)
        t1 = time.time()
        print(f'Runtime took {t1 - t0} seconds')
        return f
    return inner_fun


@timer
def advanced_calculations():
    for i in range(1000000000):
        pass


@timer
def advanced_calculations_v2():
    i = 0
    while i < 1000000000:
        pass
        i += 1


test_fun()
print()
test_fun_2()
print()

single = SingletonClass()
second = SingletonClass()
third = SingletonClass()
print(third.instances)
third.instances = 5
print(third.instances)

print('Let the calculations begin!')
advanced_calculations()
advanced_calculations_v2()
