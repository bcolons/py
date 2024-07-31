import asyncio
'''Code adapted from: (recursion added...sleep(0) line modified, comments etc...)
    /mnt/c/Users/bcollins/pyd/library/asyncio-task.html#running-tasks-concurrently
'''

async def factorial(name, number,await_flg):
    print(f"Task {name}: Compute factorial({number})...")
    if(await_flg):
        await asyncio.sleep(0)   # returns execution to event loop allowing other guys to execute and changing order of execution from sequential (ABC) to round robin or shortest-in-first-out (least awaited, first out LAFO---'lazy-factorial')
    if(number != 1):
        return number*(await factorial(name, number-1,await_flg)) #await is not lazy...schedules and runs r.h. block an initial time, and all the way unless interrupted/dispatched to event loop via asyncio.sleep
    else:
        return 1

async def main(flag=False):
    # Schedule three calls *concurrently*:
    L = await asyncio.gather(
        factorial("A", 2,flag),
        factorial("B", 3,flag),
        factorial("C", 4,flag),
        factorial("D", 5,flag),
    )
    print(L)

print("...not sleep0 then sleep0'd btwn recursions...")
asyncio.run(main())
asyncio.run(main(True))
