import asyncio
import time
def read1(fd):
    return fd.read(1)

async def main():
    with open('/dev/tty1','r') as fd: 
        while True: #multiple threads doesnt improved missed char rate...each time each of the four awaits returns the main loop has to run
            print('first one'+str( await asyncio.to_thread(read1, fd)))
            print('second one'+str( await asyncio.to_thread(read1, fd))) 
            print('third one'+str( await asyncio.to_thread(read1, fd))) 
            print('fourth one'+str( await asyncio.to_thread(read1, fd))) 
asyncio.run(main())

