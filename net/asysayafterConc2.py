import asyncio
import time

async def say_after(delay, what):
    print('before'+what)
    await asyncio.sleep(delay)
    print('afdter'+what)
    #await say_after(delay, what) # ---when uncommented  this forkbombs 'hello' ...with 1s delay!!!

async def main():
    print(f"started at {time.strftime('%X')}")
    for i in range(4): # forloop awaits for the awaits before looping, why?
        i+=1
        await asyncio.create_task( say_after(i, str(i)+'hello'))
        await asyncio.create_task( say_after(i, str(i)+'world'))

    print(f"finished at {time.strftime('%X')}")

asyncio.run(main(),debug=True)
#template: async def f1(delay): await asyncio.sleep(delay)
#template: async def f2(): await f1(23456), await f1(987655) #loop blocks until both return
#template: asyncio.run(f2() )
