import asyncio
'''Code from: (except sleep(0) line, etc...)
    /mnt/c/Users/bcollins/pyd/library/asyncio-task.html#running-tasks-concurrently
'''

async def factorial(name, number):
    f = 1
    for i in range(2, number + 1):
        print(f"Task {name}: Compute factorial({number}), currently i={i}...")
        await asyncio.sleep(0)   # returns execution to event loop allowing other guys to execute and changing order of execution from sequential (ABC) to round robin or shortest-in-first-out (least awaited, first out LAFO---'lazy-factorial')
        # here is an example of near-recursion using await to play nice with other gather()'d coro's
        f *= i
    print(f"Task {name}: factorial({number}) = {f}")
    return f

async def main():
    # Schedule three calls *concurrently*:
    L = await asyncio.gather(
        factorial("A", 2),
        factorial("B", 3),
        factorial("C", 4),
    )
    print(L)

asyncio.run(main())
