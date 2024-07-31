import asyncio
import time
'async to unblock a normal blocking read(1), recursing to await sbsq char' 
async def read1(fd,me_id):
    print(fd.read(1)+me_id)
    #await asyncio.sleep(0)
    await read1(fd,me_id)

async def main():
    with open('/dev/tty1','r') as fd: 
        await read1(fd,'1')
        await read1(fd,'2')
        await read1(fd,'4')
        await read1(fd,'5')
        await read1(fd,'6')
        await read1(fd,'7')
        await read1(fd,'8')
        await read1(fd,'9')
        await read1(fd,'3') #does not seem to improve char miss rate, only me_id=='1' is ever awaited....
asyncio.run(main())

