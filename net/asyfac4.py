import asyncio

async def factorial(name, number):
    f = 1
    for i in range(2, number + 1):
        print(f"Task {name}: Compute factorial({number}), currently i={i}...")
        await asyncio.sleep(5-number)
        f *= i
    print(f"Task {name}: factorial({number}) = {f}")
    return f

async def main():
    # Schedule three calls *concurrently*: larger nums require more sleep / th4 time
    iterfun=iter([ factorial("fac2", 2), factorial("fac3", 3),factorial("fac4", 4)])

    # 'Run awaitable objects in the aws iterable concurrently. Return an iterator of coroutines. Each coroutine returned can be awaited to get the earliest next result from the iterable of the remaining awaitables.'
    # BC--this iterator keeps on giving awaitable elems, which we await -for...

    iterable_coros= asyncio.as_completed(iterfun) # each of the three added to event loop 
    print("someone's DONE!!")
    #earliest_result=await next(iterable_coros) #the first coro  is the first coro to return from its last await...only to to be await'd on again ...which returns the result.
    #earliest_result=await next(iterable_coros) #the first coro  is the first coro to return from its last await...only to to be await'd on again ...which returns the result.
    #earliest_result=await next(iterable_coros) #the first coro  is the first coro to return from its last await...only to to be await'd on again ...which returns the result.
    # 'calling await' submits the current block/context to the event loop, typically pausing execution, eventually the 'await call' re-enters the block just below the await'd in the block, calling await again continues normal blocking execution until the function actually returns. (or maybe an await-return would typically involve calling a callback but with as_completed it each 'await-return' is delivered as an iterator of callables in leiu of having a callback (tail-callback?)
    print('its'+str(earliest_result))
asyncio.run(main())
#template: async def f1: await asyncio.sleep(1), mathstuff()
#template: async def f2: 
#template:    i=iter(f1(abc),f1(def),f1(ghi)
#template:    for elem in asyncio.as_completed(i): 
#template:       earliest_result=await elem
#template: asyncio.run(f2())
