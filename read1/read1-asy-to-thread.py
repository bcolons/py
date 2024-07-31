import asyncio
import time
def read1(fd):
    return fd.read(1)

async def main():
    with open('/dev/tty1','r') as fd: 
        while True:
            print( await asyncio.to_thread(read1, fd)) # does not thread-bomb...each while loop iteration only commences once await returns (asynch-sequential)
asyncio.run(main())

