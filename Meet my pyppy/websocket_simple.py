import asyncio
import aiohttp


session = aiohttp.ClientSession()       # handles the context manager


class EchoWebsocket:

    # this part doesn't work I guess
    async def connect(self):
        self.websocket = await session.ws_connect("wss://echo.websocket.org")

    async def send(self, message):
        self.websocket.send_str(message)

    async def receive(self):
        result = await self.websocket.receive()
        return result.data


async def main():
    echo = EchoWebsocket()
    await echo.connect()
    await echo.send(message="hello, world")
    print(await echo.receive())


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
