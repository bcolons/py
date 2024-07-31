import time 
import asyncio as asy
class Timer:
    '''Single not threadsafe class to get time and return delta time since last get_time()
    With 'async with lock: ...time.sleep(9)' this becomes some of the shittiest blocking code in an otherwise speedy concurrent run...
    loop has to do nothing to run down the clock on the lock, releasing it'''
    t=time.time()
    @staticmethod
    async def gettime():
        lock=asy.Lock()
        async with lock: 
            tmp=time.time() 
            delta=tmp-Timer.t
            #asy.sleep(10)
            time.sleep(9)
            Timer.t=tmp
            return tmp,delta
if(__name__=='__main__'):
    with Timer() as a:
        print(Timer.gettime())
        time.sleep(1)    
        print(Timer.gettime())
