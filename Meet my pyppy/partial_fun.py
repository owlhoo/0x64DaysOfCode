from functools import partial


def fun_1(fun_2, arg):
    fun_2(arg)
    print("fun 1 done")


def fun_2(arg0, arg1):
    print(f"fun2({arg0}, {arg1})")
    return


def main():
    # partial return function with one (i.e.) positional argument less
    nfun_2 = partial(fun_2, "hello",)
    fun_1(nfun_2, "world")


if __name__ == "__main__":
    main()
