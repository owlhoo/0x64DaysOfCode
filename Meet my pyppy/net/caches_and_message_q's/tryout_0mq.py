import zmq
import threading
import time


def pull_pipeline(zcontext, url):
    zsock = zcontext.socket(zmq.PULL)
    zsock.bind(url)

    while True:
        message = zsock.recv_string()
        print(f'Pull consumer received "{message}"')


def push_pipeline(zcontext, ourl, ids, message):
    osock = zcontext.socket(zmq.PUSH)
    osock.connect(ourl)
    osock.send_string(f'producer {ids} says "{message}"')
    print(f'producer {ids} sent its message..')


def start_thread(func, *args):
    thread = threading.Thread(target=func, args=args)
    thread.daemon = True
    thread.start()


if __name__ == '__main__':
    mailbox_address = 'tcp://127.0.0.1:9151'
    context = zmq.Context()

    start_thread(pull_pipeline, context, mailbox_address)
    for i in range(5):
        start_thread(push_pipeline, context, mailbox_address, i, 'Hello, world from ' + str(i))

    time.sleep(5)


