import asyncio

bgtasks=set()
notprimes=[]

async def genRainbow(x,last,maxnum):
    await asyncio.sleep(1)
    xx=x*last
    notprimes.append( xx)
    if( xx < maxnum):
        genRainbow(x,xx,maxnum)

async def dump_not_primes():
    await asyncio.sleep(5)
    print(notprimes)

loop=asyncio.get_running_loop()
for i in range(1000):
    task=asyncio.create_task(genRainbow(i,1, 2000))
    bgtasks.add(task)
    task.add_done_callback(bgtasks.discard)

asyncio.run(main())
