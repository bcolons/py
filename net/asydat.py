import asyncio
import datetime

async def display_date():
    loop = asyncio.get_running_loop()
    end_time = loop.time() + 5.0
    while True:
        print(datetime.datetime.now())
        if (loop.time() + 1.0) >= end_time:
            break
        await asyncio.sleep(1)

asyncio.run(display_date())

#template: shows asyncio.get_running_loop().time()
#template: async def f1: loop=asyncio.get_running_loop(), while True: stuff, await asyncio.sleep(123)
#template: asyncio.run(f1())
