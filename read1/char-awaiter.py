import asyncio
import sys
import time
import subprocess
import re
import time


'Uses async to unblock normal blocking read(1) and write calls (still loses rapidly entered characters in input....why?) '

async def aaread1(fd,fdo):
    char= fd.read(1)
    await aread1(fd,fdo)
    await awrite1(fd,fdo,char,int(char))
async def aread1(fd,fdo):
    char=fd.read(1)
    await awrite1(fd,fdo,char,int(char))
    await aread1(fd,fdo)

async def awrite1(fd,fdo,char,nleft):
    if(nleft>0):
        fdo.write(char)
        fdo.flush()
        #time.sleep(.1)
        await awrite1(fd,fdo,char,nleft-1)
def write1(fd,fdo,char,nleft):
    if(nleft>0):
        fdo.write(char)
        fdo.flush()
        write1(fd,fdo,char,nleft-1)
    
async def main():
    try:
        sys.argv[1]
    except IndexError:
        print('usage: \n python char-interacter-async.py /dev/tty2 \n( or some alternate tty for character input and output)')
        return -1

    #with open('/dev/tty2','r') as fd: 
    with open(sys.argv[1],'r') as fd: 
        with open(sys.argv[1],'w') as fdo: 
            await aread1(fd,fdo)
asyncio.run(main())

