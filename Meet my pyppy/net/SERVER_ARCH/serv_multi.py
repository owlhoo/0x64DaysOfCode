import time

import routines_zen
from threading import Thread, enumerate


def start_threads(listener, workers=4):
    t = (listener,)

    for i in range(workers):
        threads.append(Thread(target=routines_zen.accept_connections_forever, args=t))
        threads[i].start()


def check_alive(workers=4):
    while True:
        if len(enumerate()) != workers + 1:             # worker + one main thread
            print('A thread has died. :(')
        time.sleep(3)


if __name__ == '__main__':
    address = routines_zen.parse_command_line('multi-threaded server')
    listener = routines_zen.create_srv_socket(address)
    threads = []
    start_threads(listener)
    check_alive()
