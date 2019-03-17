import asyncio
from time import sleep


async def first():
    print("first started")
    for i in range(10):
        await asyncio.sleep(1.5)
        print(f'first {i}')


async def second():
    print("second started")
    for i in range(15):
        await asyncio.sleep(1)
        print(f'second {i}')


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    # loop.run_until_complete(main())
    fun = asyncio.wait([first(), second()])
    loop.run_until_complete(fun)
