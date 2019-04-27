import zmq
import argparse


context = zmq.Context()


def sub():
    subscriber = context.socket(zmq.REQ)
    subscriber.connect("tcp://localhost:5555")

    # subscriber.setsockopt(zmq.REQUEST, "Hello".encode('ascii'))
    subscriber.send(b'Hello')
    message = subscriber.recv()
    print(message)


def pub():
    publisher = context.socket(zmq.REP)
    publisher.bind("tcp://*:5555")
    text = input('Enter some message to be sent to the subscribers:\n').encode('ascii')
    publisher.recv()
    publisher.send(text)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="0mq messaging queue")

    parser.add_argument('role', choices={'Subscriber': sub, 'Publisher': pub},
                        help="Choose should you be an publisher or subscriber")
    args = parser.parse_args()
    fun = {'Subscriber': sub, 'Publisher': pub}.get(args.role)
    fun()
