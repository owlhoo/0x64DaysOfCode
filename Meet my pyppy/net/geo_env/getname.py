import socket


if __name__ == "__main__":
    hostname = "www.google.com"
    addr = socket.gethostbyname(hostname)
    print(f'The ip address of {hostname} is {addr}')
