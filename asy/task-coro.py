import asyncio as a
import time as t
'asynchronous-sequence ... attempt to add a timer/await-sleep loop never finishes; need asynch-concurrent gather()/as_completed()'
async def sleep1():
    await a.sleep(11)
async def sleep2():
    await a.sleep(12)
async def sleep3():
    await a.sleep(13)
async def sleep4():
    await a.sleep(14)
async def tenther(loop):
    while True:
        print(loop.time())
        await a.sleep(1)
async def go():
    l=a.get_running_loop()
    tasks=[]
    for i in [tenther(l),sleep1(),sleep2(),sleep3(),sleep4()]:
        await i
#        tasks.append( a.create_task(i))
#    for task in tasks:
#        await task
        for each in a.all_tasks():
            print(str(each))
        print('sleep 1')
        t.sleep(1)
a.run(go())
