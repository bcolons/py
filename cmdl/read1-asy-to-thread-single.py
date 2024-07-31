import asyncio
import time
def read1(fd):
    '''Simple asyncio.to_thread(..) example, '''
    #time.sleep(1) #print(fd.read(1))
    return fd.read(1)

async def main():
    with open('/dev/tty1','r') as fd: 
        await asyncio.gather( asyncio.to_thread(read1, fd))
asyncio.run(main())

