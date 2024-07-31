import asyncio
import time
class D:
    '''Global or singleton for easier cross thread data member.
    Program is a very simple template for running a method in a thread alongside an interactive listener thread.
    A purer approach has just threads and not need async.sleep0, not define a coro, not use singleton (see *-pure.py)
    '''
    d=0
def listen():
    while True:
        inp=input()
        print(f'level__{D.d}__: higuy: '+str(inp))

async def crunch():
    for i in range(9):
        D.d=i # export member to make it available for listen interrogation
        print(f'{i} of 9')
        await asyncio.sleep(1) #sleep0 is for interrupting a real world loop

async def main():
    await asyncio.gather(
        asyncio.to_thread(listen),
        crunch(),)
asyncio.run(main())

