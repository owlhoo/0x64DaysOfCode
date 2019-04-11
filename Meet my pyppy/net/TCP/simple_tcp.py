import argparse
import socket


def recvall(sock, length):
    data = b''
    while len(data) < length:
        more = sock.recv(length - len(data))
        if not more:
            raise EOFError(f'Was expecting {length} bytes '
                           f'but only received {len(data)} bytes before the socket closed')
        data += more
        return data


def server(interface, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((interface, port))
    sock.listen(1)
    print(f'Listening at {sock.getsockname()}')

    while True:
        sc, sockname = sock.accept()
        print(f'We have accepted connection from {sockname}')
        print(f'  Socket name: {sc.getsockname()}')
        print(f'  Socket peer: {sc.getpeername()}')
        message = recvall(sc, 16)
        print(f'  Incoming 16 bytes message: {repr(message)}')
        sc.sendall(b'Farewell, client')
        sc.close()
        print('  Reply sent, socket closed')


def client(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    print(f'Client has been assigned socket name {sock.getsockname()}')
    sock.sendall(b'Hi there, server, I am longer than the 16 bytes :)')
    reply = recvall(sock, 16)
    print(f'The server said {repr(reply)} and it has {sock.getpeername()} adress')
    sock.close()


if __name__ == '__main__':
    choices = {'client': client, 'server': server}
    parser = argparse.ArgumentParser(description='Simple TCP client/server program')
    parser.add_argument('role', choices=choices, help='Which role to play')
    parser.add_argument('host', help='interface the server listens at; host the client sends to')
    parser.add_argument('-p', metavar='PORT', type=int, default=1060, help='TCP port (default 1060)')
    args = parser.parse_args()
    function = choices[args.role]
    function(args.host, args.p)
