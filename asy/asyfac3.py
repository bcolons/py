import asyncio

async def factorial(name, number):
    f = 1
    for i in range(2, number * 2):
        print(f"Task {name}: Compute factorial({number}), currently i={i}...")
        await asyncio.sleep(10-number)
        f *= i
    print(f"Task {name}: factorial({number}) = {f}")
    return f
async def time_barf(loop):
    while(True):
        print( loop.time())
        await asyncio.sleep(1)
async def main():
    # Schedule three calls *concurrently*: larger nums require more sleep / th4 time
    loop=asyncio.get_running_loop()
    iterfun=iter([time_barf(loop), factorial("fac2", 2), factorial("fac3", 3),factorial("fac4", 4),time_barf(loop)])

    # 'Run awaitable objects in the aws iterable concurrently. Return an iterator of coroutines, if any is awaited, all will be run

    for coro in asyncio.as_completed(iterfun):# each of the three scheduled in event loop, in no particular order (although seemingly the last one is run first)
        print('topof-for: '+str(loop.time()))
        earliest_result=await coro #three concurrent asynchronous assignments to the same keyword-var, first time in for-loop  the first await starts all as_completed( awaitables)
        # first await begins, loop runs then first result is assigned, then  print is called and loop runs again, etc....
        print("someone's DONE!!")

        # 'calling await' submits the current block/context to the event loop, typically pausing execution, eventually the 'await call' re-enters the block just below the await'd in the block, calling await again continues normal blocking execution until the function actually returns. (or maybe an await-return would typically involve calling a callback but with as_completed it each 'await-return' is delivered as an iterator of callables in leiu of having a callback (tail-callback?)
        print('its'+str(earliest_result))
asyncio.run(main())
#template: async def f1: await asyncio.sleep(1), mathstuff()
#template: async def f2: 
#template:    i=iter(f1(abc),f1(def),f1(ghi)
#template:    for elem in asyncio.as_completed(i): 
#template:       earliest_result=await elem
#template: asyncio.run(f2())
