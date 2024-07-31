import asyncio as a
import time as t
'asynch-concurrent ex with as_completed()...all_tasks() shows callbacks, running status, coro name, task name, etc...'
async def sleep1():
    await a.sleep(1)
    return 1
async def sleep2():
    await a.sleep(2)
    return 2
async def sleep3():
    await a.sleep(13)
    return 13
async def sleep4():
    await a.sleep(14)
    return 14
async def tenther(loop):
    while True:
        print(loop.time())
        await a.sleep(.1)
async def go():
    l=a.get_running_loop()
    tasks=[]
    for i in a.as_completed([tenther(l),sleep1(),sleep2(),sleep3(),sleep4()]): # I Concur, baby!
        first=await i 
        print('done '+str(first)) # print return vals, if any
        for each in a.all_tasks():
            print(str(each))
a.run(go())
