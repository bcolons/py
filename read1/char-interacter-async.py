import asyncio
import sys
import time
import subprocess
import re


'Uses async to unblock a normal blocking read(1), recursing to await sbsq char. In a way this has two threads, an I/O tty and the main tty' 
async def read1(fd,fdo):
    char=fd.read(1)
    if(char=='q'):
        return 0
    elif(char=='x'):
            fdo.write('explain!')
            fdo.flush()
    elif(char=='h'):
        await help(fd,fdo)
    else:
            fdo.write('nothing...')
            fdo.flush()
    await read1(fd,fdo)

async def help(fd,fdo):
    fdo.write('q- quit\nh h - help\n x -explain')
    stdo=subprocess.run(['grep','def.*(.*):',sys.argv[0]],capture_output=True)
    lines=re.split('\\n',str(stdo))
    for line in lines:
        fdo.write(line+'\n') 
    
async def main():
    try:
        sys.argv[1]
    except IndexError:
        print('usage: \n python char-interacter-async.py /dev/tty2 \n( or some alternate tty for character input and output)')
        return -1

    #with open('/dev/tty2','r') as fd: 
    with open(sys.argv[1],'r') as fd: 
        with open(sys.argv[1],'w') as fdo: 
            await read1(fd,fdo)
asyncio.run(main())

