import memcache
import random
import time
import timeit

# Up-to-date data with other data in the system (i.e. database)
# should be accomplished with flush or expiration date on item
# or even invalidate only the data that is stale :)


def compute_square(mc, n):
    value = mc.get(f'sq:{n}')
    if value is None:
        time.sleep(1e-3)                    # simulate computing of a square
        value = n * n
        mc.set(f'sq:{n}', value, time=5)    # 5 seconds expiration date, default=0
    return value


def main():
    mc = memcache.Client(['127.0.0.1:11211'])

    def make_request():
        compute_square(mc, random.randint(0, 5000))

    print('Ten successive runs:')
    for i in range(1, 11):
        print('%.2fs ' % timeit.timeit(make_request, number=2000), end='')
    print()


if __name__ == '__main__':
    main()
