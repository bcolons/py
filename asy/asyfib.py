import asyncio as asy
import time as t
class sharedNum:
    n=0
async def fib_rec(num):
    print('rady set go!')
    print(num)
    if(num>1):
        #await asy.sleep(0)
        t.sleep(1)
        print('not return fib_rec('+str(num)+'-1)+fib_rec('+str(num)+'-2)')
        await fib_rec(num-1) + await fib_rec(num-2) # await bomb
    else:
        return 1
async def sub_rec(num):
    '''subtract up to and including...'''
    docstr='''subtract up to and including...'''
    print(docstr)
    print(num)
    if(num>0):
        #await asy.sleep(0)
        #t.sleep(1)
        sharedNum.n-=num
        await sub_rec(num-1)  # does not share with sum_rec...ends up running sequenctially, one recursive call and then the other...maybe i should gather....
    else:
        print(sharedNum.n)

async def sum_rec(num):
    '''sum up to and including...'''
    docstr='''sum up to and including...'''
    print(docstr)
    print(num)
    if(num>0):
        #await asy.sleep(0)
        #t.sleep(1)
        sharedNum.n+=num
        await sum_rec(num-1) 
    else:
        print(sharedNum.n)
async def main():
    loop= asy.get_running_loop()
    await asy.gather(sum_rec(9),sub_rec(9))
    #for coro in asy.as_completed([sum_rec(9),sub_rec(9)]):
    #    earlah=await coro
    #loop.create_task(sum_rec(9))
    #loop.create_task(sub_rec(9))
    #loop.create_task(fib_rec(9))

asy.run(main())

# 1,1,2,3,5,8,13

#fib(1)==1
#fib(2)==1+1
#fib(1)==1
#fib(1)==1
#fib(1)==1
#fib(1)==1
#fib(1)==1

