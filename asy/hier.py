import asyncio
import time as t
import logging as lgn

def elementer(*a): 
    '''print elems in a sequence of literals or functions, does not eval'''
    for elem in a: # calls iterator.__iter__(a)
        print(elem) # does not eval if 'a' is generator instance

def iterater(a):
    '''evaluate iterations of a sequence of literals or functions and print result'''
    for elem in a:
        print(elem)  # does evel when a is a generator instance

def callable_seq_generater(func,seq):
    '''return a list of callables that is the same length as seq'''
    out=[]
    for elem in seq:
        out.append(lambda x: func(x))
    return out

async def sum_down_from_nr(x,cur): 
    '''a recursive func that doesn't use return value'''
    print(t.time())
    t.sleep(1)
    if(x!=0):
        print( cur)
        await sum_down_from(x-1, cur+x)
    else:
        print( cur)
 
async def sum_down_from(x,cur): 
    '''a recursive func that does use return value, which is lost ....'''
    print(t.time())
    if(x!=0):
        t.sleep(2)
        print( cur)
        await sum_down_from(x-1, cur+x)
    else:
        return cur
 
def two_timer(a):
    return 2*a

def list_comprehenser(func,seq): # shorthand is [ func(out_seq) for outseq in seq ] 
    '''evaluate stepwise iterations of a function and a sequence of argument values'''
    outseq=[]
    for elem in seq:
        outseq.append(func(elem))
    return outseq

def generic_generater(func,seq): # shorthand is ( func(elem) for elem in seq )
    '''yield iterations of a function and sequence of argument values
     (it's a lazy list!) '''
    for elem in seq:
        yield func(elem)

async def func_loafer(func, delay=91,*args):
    '''iterates 'await func(*args) interleaved with asyncio.sleep(delay)'s'''
    print(t.time())
    func(args) #this guy should await itself...
    await asyncio.sleep(delay)
async def timer(loop):
    print(loop.time())
    await asyncio.sleep(3)

async def main():
    a = [1,2,3,4] 
    loop = asyncio.get_running_loop()
    loop.set_debug(True)
    lgn.getLogger('asyncio').setLevel(lgn.DEBUG)
    for coro in asyncio.as_completed(iter([sum_down_from(5,0)])):
        retval= await coro
    print('retval: '+retval.result)
    #loop.create_task( sum_down_from(5,0))
    #loop.create_task(timer(loop))
    
    b = (1,2,3,4)
    d = {1,2,3,4}
    #e =  list_comprehenser(a,two_timer)
    #f =  [two_timer(out) for out in a]
    #i=callable_seq_generater(a,two_timer)
    #j = [elem[0](elem[1]) for elem in zip(i,a)]
    #print(j)

asyncio.run(main(),debug=True)
# template: aysyncio.run(f1()
# template: async def f1():
# template:   loop.asyncio.get_running_loop()
# template:  ... #some initialization or checks here...run only once
# template:   loop.creat_task( f2()) #schedules task, executes until first await, and 'immediately' continues below....
# template:   loop.create_task( f3()) # f3() doesnt start/complete/suspend -running in any way linked to f2()
# template:  ...# 'finally' once both return from final 'await' 
# template:  async def f2():
# template:  ... #before awaiting first time, then second, etc...
# template:   await some_blocking_io_or_async.builtin()
# template:  ...# await returns once, then second time, etc... 
# template:  async def f3():
# template:  ... #before awaiting first time, then second, etc...
# template:   await some_other_blocking_io_or_async.builtin()
# template:  ...# await returns once, then second time, etc... 
# template:  ...
# template: 

