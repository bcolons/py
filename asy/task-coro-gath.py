import asyncio as a
import time as t
'gather(coros) example...no task metadata to see'
async def sleep1():
    await a.sleep(1)
async def sleep2():
    await a.sleep(2)
async def sleep3():
    await a.sleep(13)
async def sleep4():
    await a.sleep(14)
async def tenther(loop):
    while True:
        print(loop.time())
        await a.sleep(2)
async def go():
    l=a.get_running_loop()
    tasks=[]
    c=tenther(l)
    print(c.cr_origin)
    L = await a.gather(sleep1(),sleep2(),sleep3(),sleep4())
    #for each in a.all_tasks(): # coro's are not tasks....nothing to see here 
    for each in L: # coro's are not tasks....nothing to see here 
        print(each.cr_origin)
a.run(go())
