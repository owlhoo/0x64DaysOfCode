import asyncio

import functools

# event trigger function "gunshot at the race"


def trigger(event):
    print('EVENT SET')
    event.set()  # wake up coroutines waiting


# event consumers
async def consumer_a(event):
    consumer_name = 'CONSUMER A'
    print(f'{consumer_name} waiting.')
    await event.wait()
    print(f'{consumer_name} triggered')


async def consumer_b(event):
    consumer_name = 'CONSUMER B'
    print(f'{consumer_name} waiting.')
    await event.wait()
    print(f'{consumer_name} triggered')

# event
event = asyncio.Event()

# wrap coroutines in one future
main_future = asyncio.wait([consumer_a(event), consumer_b(event)])

# event loop
event_loop = asyncio.get_event_loop()
event_loop.call_later(0.1, functools.partial(trigger, event))  # trigger event in 0.1 sec

# complete main_future
done, pending = event_loop.run_until_complete(main_future)
