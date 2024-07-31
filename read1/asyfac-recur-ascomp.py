import asyncio
'''Code adapted from: (recursion added...sleep(0) line modified, comments etc...)
    /mnt/c/Users/bcollins/pyd/library/asyncio-task.html#running-tasks-concurrently
'''

async def factorial(name, number,await_flg):
    print(f"Task {name}: Compute factorial({number})...")
    if(await_flg):    
        await asyncio.sleep(0)   # returns execution to event loop allowing other guys to execute and changing order of execution from as_completed_indeterminate (BCAD) to round robin or shortest-in-first-out (least awaited, first out LAFO---'lazy-factorial')
    if(number != 1):
        return number*(await factorial(name, number-1,await_flg)) #await is not lazy...schedules and runs r.h. block an initial time, pushing new await frame (for *later* await-ment) onto prog stack each time
    else:
        return 1

async def main(flag=False):
    # Schedule three calls *concurrently*:
    L = asyncio.as_completed(iter([
        factorial("A", 2,flag),
        factorial("B", 3,flag),
        factorial("C", 4,flag),
        factorial("D", 5,flag),
    ]))
    for coro in L:
        print( await coro)

print("...not sleep0 then sleep0'd btwn recursions")
asyncio.run(main())
asyncio.run(main(True))
