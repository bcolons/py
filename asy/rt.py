import asyncio as a
async def main_gath():
    'Exploring realtime scheduling with event loop. Attempt to print time at exactly new second boundaries....tolerance goes to about +.002'
    T = a.gather(ln(1),ln(2),ln(3)) # scheduled and run immeditely, one must be awaited to avoid 'never-awaited' complaint
#    await T # obviously what is supposed to happen while true await sleep compalins
    while True:
        await a.sleep(1)
async def main_ascomp():
    for coro in a.as_completed([ln(1),ln(2),ln(3)]): # await any, and you'll await them all.... a.sleep() gives 'never-awaited' complaint
        await coro # obviously what is supposed to happen
        #await  a.sleep(1)
async def ln(n):
    loo=a.get_running_loop()
    newdelta=0
    while True:
        now=loo.time()
        newdelta=now-(now//1)
        ceil=1-newdelta
        print('l'+str(n)+': '+str(now)+'delta: '+str(newdelta/2))
        if(ceil >= newdelta):
            await a.sleep( n - newdelta/2)
        else:
            await a.sleep( n - 1 + ceil/2 ) # went below floor, get things back on the up and up
a.run(main_ascomp())
