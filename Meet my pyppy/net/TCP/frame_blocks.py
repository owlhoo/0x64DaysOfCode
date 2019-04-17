import socket
import struct
from argparse import ArgumentParser

header_struct = struct.Struct('!I')     # messages up to 2**32 - 1 length


def recvall(sock, length):
    blocks = []
    while length:
        block = sock.recv(length)
        if not block:
            raise EOFError(f'socket closed with {length} bytes'
                           f'left in this block')
        length -= len(block)
        blocks.append(block)
    return b''.join(blocks)


def get_block(sock):
    packed_block_len = recvall(sock, header_struct.size)
    (block_length,) = header_struct.unpack(packed_block_len)
    return recvall(sock, block_length)


def put_block(sock, message):
    block_len = len(message)
    sock.send(header_struct.pack(block_len))
    sock.send(message)


def server(address):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    sock.bind(address)
    sock.listen(1)
    print(f'Run this script in another windows with "-c" to connect')
    print(f'Listening at {sock.getsockname()}')

    sc, sockname = sock.accept()
    print(f'Accepted connection from {sockname}')
    sc.shutdown(socket.SHUT_WR)
    while True:
        block = get_block(sc)
        if not block:
            break
        print(f'Block says {repr(block)}')
    sc.close()
    sock.close()


def client(address):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(address)
    sock.shutdown(socket.SHUT_RD)
    put_block(sock, b'1. Beautiful is better than ugly')
    put_block(sock, b'2. Beautiful is better than ugly')
    put_block(sock, b'3. Beautiful is better than ugly')
    put_block(sock, b'')
    sock.close()


if __name__ == '__main__':
    parser = ArgumentParser(description='Transmit and receive blocks over TCP')
    parser.add_argument('hostname', nargs='?', default='127.0.0.1')
    parser.add_argument('-c', action='store_true', help='run as the client')
    parser.add_argument('-p', type=int, metavar='port', default=1060,
                        help='TCP port number (default: %(default)s')
    args = parser.parse_args()
    fun = client if args.c else server
    fun((args.hostname, args.p))
