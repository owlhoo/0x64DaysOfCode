def function_change(f):
    def func_ret_l1(*args):
        return f(*args) - 1
    return func_ret_l1


@function_change
def add(x, y):
    return x + y


print(add(5, 2))
