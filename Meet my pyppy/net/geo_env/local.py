import os
import socket
import http.client


def connect_http(address):
    client = http.client.HTTPConnection(address)
    client.request('GET', '/')

    raw_reply = client.getresponse().read()

    print(raw_reply)
    with open('neki_fajl.html', 'w') as file:
        file.write(raw_reply.decode('utf-8'))


def kek(address):
    sock = socket.socket()
    sock.connect((address, 80))
    request = "GET / \r\n\r\n"
    sock.sendall(request.encode('ascii'))
    raw_reply = b''

    while True:
        more = sock.recv(4096)
        if not more:
            break
        raw_reply += more

    print(raw_reply.decode('utf-8'))


if __name__ == "__main__":
    kek('192.168.1.1')
    # connect_http('192.168.1.1')

