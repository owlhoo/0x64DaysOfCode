import multiprocessing
import threading
import time
from random import randint


def count_up():
    i = 0
    while i <= 3:
        print(f'UP:\t{i}')
        time.sleep(randint(1, 3))
        i += 1


def count_down():
    i = 3
    while i >= 0:
        print(f'DOWN:\t{i}')
        time.sleep(randint(1, 3))
        i -= 1


def thready():
    print('Hello, world!')


if __name__ == '__main__':
    workerUp = multiprocessing.Process(target=count_up)
    workerDown = multiprocessing.Process(target=count_down)
    mythread = threading.Thread(target=thready)

    workerUp.start()
    workerDown.start()

    workerUp.join()
    workerDown.join()

    mythread.start()

    mythread.join()

