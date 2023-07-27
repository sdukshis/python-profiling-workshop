import time
import asyncio

def do_nothing():
    pass


def busy_wait(duration):
    end_time = time.time() + duration

    while time.time() < end_time:
        do_nothing()


async def foo():
    while True:
        await asyncio.sleep(1)
        busy_wait(0.1)


async def bar():
    while True:
        await asyncio.sleep(1)
        busy_wait(0.2)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()

    loop.create_task(foo())
    loop.create_task(bar())

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    loop.close()
