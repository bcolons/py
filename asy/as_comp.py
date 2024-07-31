import asyncio as asy
import time as t
from timer import Timer as T
async def main():
    loop=asy.get_running_loop()
    for coro in asy.as_completed([f1(loop),f2(loop),f3(loop)],timeout=30):
        earlah=await coro
        print(earlah)
def time_barf(loop):
        del1=t.time()
        del2=loop.time()
        print(' t.time: '+ str(del1)+' loop.time: '+ str(del2),end='')
        del1=t.time()-del1
        del2=loop.time()-del2
        print(' del t.tim: '+str(del1)+' del loop.t: '+str(del2),end='')
async def atime_barf(loop):
    while(True):
        print('loop.t: '+ str( loop.time()))
        await asy.sleep(0)

async def f3(loop):
    ct=0
    while True:
        ct+=1
        #t.sleep(1) # greedy blocked up fucker! ...slows everyone; although with a blocking lock(3secs) he's wasting time that needs to be wasted....
        print(str(ct)+ ' startig another f3 loop...')
        await T.gettime()
        await asy.sleep(0) 
        #print(T.gettime())
        print('completing another f3 loop...')
async def f2(loop):
    ct=0
    while True:
        ct+=1
        print(str(ct)+ ' startig another f2 loop...')
        #await T.gettime() # dont need no stinkin' locks!
        await asy.sleep(1) # a scholar and a gentle thread!, even without the blocking lock in Timer for the other two coros...still lowest number of cycles
        #print(T.gettime())
        print('completing another f2 loop...')
async def f1(loop):
    ct=0
    while True:
        ct+=1
        print(str(ct)+ ' startig another f1 loop...')
        await T.gettime()
        await asy.sleep(0) # agnostic about everyone else, live and let live
        #print(T.gettime())
        print('completing another f1 loop...')
asy.run(main())
