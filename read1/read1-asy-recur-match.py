import asyncio
import time
'async to unblock a normal blocking read(1), recursing to await sbsq char' 
async def read1(fd):
    char=fd.read(1)
    if(char=='q'):
            print('quit! ...use CTRL-c')
    elif(char=='x'):
            print('explain!')
    elif(char=='h'):
            print('help....')
    else:
            print('nothing...')
    await read1(fd) # probably mistaken, really want a while True: asyncio.fd.read equiv

async def main()s:
    with open('/dev/tty2','r') as fd: 
        await read1(fd)
asyncio.run(main())

