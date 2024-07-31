import asyncio
import time
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
        await read1(fd,'3') #does not improve char miss rate, only me_id=='1' is ever awaited.... perhaps because we didnt gather(..) these guys...
asyncio.run(main())

