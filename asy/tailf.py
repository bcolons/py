import time as t
import asyncio as asy
async def main():
    '''    For text files with open('testfile','rb') as readable: # we need 'rb' to get bytes...to get EOF (b'')'''

    loop=asy.get_running_loop()
    loop.create_task(asy_ct_until_empty('testfile'))
    for coro in asy.as_completed([asy_ct_until_empty('testfile')]):
        hey=await coro
    ct_until_empty('testfile')
    #ct_until_empty('testfile')

def write_byte(writeable,byte):
    writeable.write(byte)
    writeable.write(b'')

def read_byte(readable,num):
    return readable.read(num)

def ct_until_empty(filen):
    with open(filen,'rb') as fd:
        #await asy.sleep(0)
        print( fd.read(1))
        #await asy.sleep(0)
        print( fd.read(1))
        #await asy.sleep(0)
        print( fd.read(1))
async def asy_ct_until_empty(filen):
    '''does not work'''
    with open(filen,'rb') as fd:
        await asy.sleep(0)
        print( fd.read(1))
        await asy.sleep(0)
        print( fd.read(1))
        await asy.sleep(0)
        print( fd.read(1))


asy.run(main(),debug=True)
