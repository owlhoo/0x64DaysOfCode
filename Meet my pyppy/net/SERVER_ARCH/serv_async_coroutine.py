import asyncio
import routines_zen


@asyncio.coroutine
def handle_conversation(reader, writer):
    address = writer.get_extra_info('peername')
    print(f'Accepted connection from {address}')
    while True:
        data = b''
        while not data.endswith(b'?'):
            more_data = yield from reader.read(4096)
            if not more_data:
                if data:
                    print(f'Client {address} sent {data} then closed')
                else:
                    print(f'Client {address} closed socket normally')
                return
            data += more_data
        answer = routines_zen.get_answer(data)
        writer.write(answer)


if __name__ == '__main__':
    address = routines_zen.parse_command_line('asyncio server using coroutine')
    loop = asyncio.get_event_loop()
    coro = asyncio.start_server(handle_conversation, *address)
    server = loop.run_until_complete(coro)
    print(f'Listening at {address}')
    try:
        loop.run_forever()
    finally:
        server.close()
        loop.close()
