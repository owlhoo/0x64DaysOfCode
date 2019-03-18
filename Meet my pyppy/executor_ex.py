import asyncio
from concurrent.futures import ThreadPoolExecutor


def func(a, b):
    return print(a + b)


async def main(loop):
    executor = ThreadPoolExecutor()
    await loop.run_in_executor(executor, func, "Hello,", " world!")
    await asyncio.sleep(1.5)
    print("I'm supposed to be waiting..")


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(loop))
