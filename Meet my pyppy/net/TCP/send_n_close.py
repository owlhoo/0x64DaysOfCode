import socket
from argparse import ArgumentParser


def server(address):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(address)
    sock.listen(1)

    print('Run this script in another window with "-c" to connect')
    print(f'Listening at {sock.getsockname()}')
    sc, sockname = sock.accept()
    print(f'Accepted connection from {sockname}')
    sc.shutdown(socket.SHUT_WR)                                     # Shuts down wr direction from this socket

    message = b''
    while True:
        more = sc.recv(8192)                                        # 8k
        if not more:                                                # socket has closed when recv returns ''
            print('Received zero bytes - end of file')
            break
        print(f'Received {len(more)} bytes')
        message += more
    print('Message\n')
    print(message.decode('ascii'))

    sc.close()
    sock.close()


def client(address):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(address)
    sock.shutdown(socket.SHUT_RD)
    sock.sendall(b'Beautiful is better than ugly.\n')
    sock.sendall(b'Explicit is better than implicit.\n')
    sock.sendall(b'Simple is better than complex\n')
    sock.close()


if __name__ == '__main__':
    parser = ArgumentParser(description='Transmit & receive a data stream (send and close)')
    parser.add_argument('hostname', nargs='?', default='127.0.0.1',
                        help='IP address or hostname (default: %(default)s)')
    parser.add_argument('-c', action='store_true', help='run as the client')
    parser.add_argument('-p', type=int, metavar='port', default=1060,
                        help='TCP port number (default: %(default)s)')
    args = parser.parse_args()
    func = client if args.c else server
    func((args.hostname, args.p))
