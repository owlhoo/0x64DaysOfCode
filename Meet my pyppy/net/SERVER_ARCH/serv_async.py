import asyncio
import routines_zen


class ZenServer(asyncio.Protocol):

    def connection_made(self, transport):
        self.transport = transport
        self.address = transport.get_extra_info('peername')
        self.data = b''
        print(f'Accepted connection from {self.address}')

    def data_received(self, data):
        self.data += data
        if self.data.endswith(b'?'):
            answer = routines_zen.get_answer(data)
            self.transport.write(answer)
            self.data = b''

    def connection_lost(self, exc):
        if exc:
            print(f'Client {self.address} error: {exc}')
        elif self.data:
            print(f'Client {self.address} sent {self.data} but then closed')
        else:
            print(f'Client {self.address} closed the socket')


if __name__ == '__main__':
    address = routines_zen.parse_command_line('asyncio server using callbacks')
    loop = asyncio.get_event_loop()
    coro = loop.create_server(ZenServer, *address)
    server = loop.run_until_complete(coro)
    print(f'Listening at {address}')
    try:
        loop.run_forever()
    finally:
        server.close()
        loop.close()
