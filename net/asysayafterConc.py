import asyncio
import time

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main():
    print(f"started at {time.strftime('%X')}")
    for i in range(4): # forloop awaits for the awaits before looping, why?
        await asyncio.create_task( say_after(i, str(i)+'hello'))
        await asyncio.create_task( say_after(i, str(i)+'world'))

    # Wait until both tasks are completed (should take
    # around 2 seconds.)

    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())
#template: async def f1(delay): await asyncio.sleep(delay)
#template: async def f2(): await f1(23456)
#template: asyncio.run(f2() )
