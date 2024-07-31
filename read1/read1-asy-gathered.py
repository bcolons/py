import asyncio
import time
async def read1(me_id):
    '''Simple asyncio.gather(..) example, read and print one char from tty2 (optionally in a recursion). '''
    with open('/dev/tty2','r') as fd:
        print(fd.read(1)+me_id)
        #await read1(fd,me_id) optional recursion; if so only '1' is ever awaited , recursion captures execution, never releases first gather()'d coro to event loop...and so cannot ever return from the other gather()'d coro...not clear if you can ever use recursive await's

async def main():
    #with open('/dev/tty2','r') as fd: # failed: fd goes out of context/frame/scope after gather even though ref count to fd !=0 ...
    L = asyncio.gather( read1('1'), read1('2') )
asyncio.run(main())

