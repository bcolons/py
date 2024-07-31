import asyncio
import time
async def read1(fd,me_id):
    print(fd.read(1)+me_id)
    #await asyncio.sleep(0)
    await read1(fd,me_id)

async def main():
    with open('/dev/tty2','r') as fd: 
        L = asyncio.as_completed([ read1(fd,'1'), read1(fd,'2') ]) # recurs! only '2' is ever awaited
        for coro in L:
            await coro
asyncio.run(main())

