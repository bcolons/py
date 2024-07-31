import asyncio
import time
def read1(fd):
    time.sleep(1) #print(fd.read(1))
    return fd.read(1)

async def main():
    with open('/dev/tty1','r') as fd: 
        while True:
            await asyncio.gather( asyncio.to_thread(read1, fd))
            print(asyncio.all_tasks())
            #print(char) ...thread bomb?
asyncio.run(main())

