import asyncio
import time

async def say_after(delay, what,i):
    await asyncio.sleep(delay)
    print(str(i)+what)
    await say_after(delay,what,i) #glacial forkbomb

async def main():
    print(f"started at {time.strftime('%X')}")

    i=1
    while(True):
        i+=1
        await say_after(i, 'hello',i)
        print('awaiting.... num: '+str(i))

    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())
#template: async def f1(delay): await asyncio.sleep(delay)
#template: async def f2(): await f1(23456)
#template: asyncio.run(f2() )
