import routines_zen


if __name__ == '__main__':
    address = routines_zen.parse_command_line('simple single-threaded server')
    listener = routines_zen.create_srv_socket(address)
    routines_zen.accept_connections_forever(listener)
