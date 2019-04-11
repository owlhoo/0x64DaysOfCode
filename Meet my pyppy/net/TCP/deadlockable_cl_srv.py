import argparse
import socket
import sys


def server(host, port, bytecount):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((host, port))
    sock.listen(1)              # 1 indicates that one client can be waiting before os rejects any new ones
    print(f'Listening at {sock.getsockname()}')
    while True:
        sc, sockname = sock.accept()
        print(f'Processing up to {bytecount} bytes at a time from {sockname}')
        n = 0
        while True:
            data = sc.recv(bytecount)
            if not data:
                break
            output = data.decode('ascii').upper().encode('ascii')
            sc.sendall(output)
            n += len(data)
            print(f'\r {n} bytes processed so far', end=' ')
            sys.stdout.flush()
        print()
        sc.close()
        print(' Socket closed')


def client(host, port, bytecount):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    bytecount = (bytecount + 15) // 16 * 16     # round up to a multiple of 16
    message = b'Capitalize this!'               # 16-byte message to repeat over and over

    print(f'Sending {bytecount} bytes of data in chunks of 16 bytes')
    sock.connect((host, port))

    sent = 0
    while sent < bytecount:
        sock.sendall(message)
        sent += len(message)
        print(f'\r {sent} bytes sent', end=' ')
        sys.stdout.flush()

    print()
    sock.shutdown(socket.SHUT_WR)

    print('Receiving all the data server sends back')

    received = 0
    while True:
        data = sock.recv(42)
        if not received:
            print(f' The first data received says {repr(data)}')
        if not data:
            break
        received += len(data)
        print(f'\r {received} bytes received', end=' ')

    print()
    sock.close()


if __name__ == '__main__':
    choices = {'client': client, 'server': server}
    parser = argparse.ArgumentParser(description='Get deadlocked over TCP')
    parser.add_argument('role', choices=choices, help='which role to play')
    parser.add_argument('host', help='interface the server listens at; '
                                     'host the client sends to')
    parser.add_argument('bytecount', type=int, nargs='?', default=16,
                        help='number of bytes for client to send to (default 16)')
    parser.add_argument('-p', metavar='PORT', type=int, default=1060,
                        help='TCP port (default 1060)')
    args = parser.parse_args()
    func = choices[args.role]
    func(args.host, args.p, args.bytecount)


