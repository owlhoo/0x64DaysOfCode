# kwargs = keyword arguments
# args = arguments lul
# only one permitted per function and kwargs should always be the last one


def test_fun(*args, **kwargs):
    print('\tFUN')
    print(f'all args {args}')
    print(f'all kwargs - {kwargs}')
    for key in kwargs:
        if isinstance(key, str):
            print('keyword is string')
        else:
            print('another one bites the dust')


def test_fun2(fun1, fun2, fun3):
    print(f"\tFUN2\nfun1 - {fun1}, fun2 - {fun2}, fun3 - {fun3}")


def test_fun3(**kwargs):
    # argument or default i.e. no argument
    print(kwargs.get('argument', 'no argument'))


def main():
    arg1 = ['hello', 'mate']
    arg2 = []
    kwargs = {'fun3': 'Boiieee', 'fun2': '3.1415926'}
    test_fun(arg2, arg1, volume=4)
    test_fun2(arg1, **kwargs)
    test_fun3()
    param = {'argument': 'First argument', }
    test_fun3(**param)


if __name__ == '__main__':
    main()
