#!/usr/bin/env python3
import argparse
import socket
import time

aphorisms = {b'Beautiful is better than?': b'Ugly.',
             b'Explicit is better than?': b'Implicit.',
             b'Simple is better than?': b'Complex.'}


def get_answer(aphorism):
    """Return the string response to a particular Zen-of-Python aphorism."""
    time.sleep(0.5)         # increase to simulate an expensive operation
    return aphorisms.get(aphorism, b'Error: unknown aphorism.')


def parse_command_line(description):
    """Parse command line and return a socket address."""
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('host', help='IP or hostname')
    parser.add_argument('-p', metavar='port', type=int, default=1060,
                        help='TCP port (default 1060)')
    args = parser.parse_args()
    address = (args.host, args.p)
    return address


def create_srv_socket(address):
    """Build and return a listening server socket."""
    listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    listener.bind(address)
    listener.listen(64)

    print(f'Listening at {address}')

    return listener


def accept_connections_forever(listener):
    """Forever answer incoming connections on a listening socket."""
    while True:
        sock, address = listener.accept()
        print(f'Accepted connection from {address}')
        handle_conversation(sock, address)


def handle_conversation(sock, address):
    """Converse with a client over 'sock' until they are done talking."""
    try:
        while True:
            handle_request(sock)

    except EOFError:
        print(f'Client socket to {address} has closed')

    except socket.timeout:
        print(f'Connection to {address} timed out and the connection has been closed.')

    except Exception as e:
        print(f'Client {address} error {e}')

    finally:
        sock.close()


def handle_request(sock):
    """Receive a single request on 'sock' and send the answer."""
    aphorism = recv_until(sock, b'?')
    answer = get_answer(aphorism)
    sock.sendall(answer)


def recv_until(sock, suffix):
    """Receive bytes over 'sock' until we receive 'suffix'."""
    sock.settimeout(2)              # set timeout to socket object

    message = sock.recv(4096)

    if not message:
        raise EOFError('socket closed')

    while not message.endswith(suffix):
        data = sock.recv(4096)
        if not data:
            raise IOError(f'received {message} then socket closed')
        message += data

    return message
