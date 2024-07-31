import asyncio
import time
'''
Program is a very simple template for running a main(..) func in a thread alongside an interactive listener thread.
Only data members may be listened too, bc_ fixme: call methods!
'''
def listen(d): # listen loop is run simultaneously with crunch
    '''Function provides an unblocked input mechanism to reveal runtime data (bc_ and call funcs!)
    '''
    while True:
        inp=input()
        print(f'crunch data in other thread: {str(d[0])},  user input is: '+str(inp))

def crunch(d): 
    ''' Placeholder for any main(..) entry point '''
    for i in range(9):
        d[0]=i # this guy available for listen interrogation
        print(f'{i} of 9')
        time.sleep(1) # placeholder for any other slow thing we might want to check in on

async def ismoke2threads(d):
    await asyncio.gather(
        asyncio.to_thread(listen,d),
        asyncio.to_thread(crunch,d),)

d=[0] # or any non-primitive used in crunch which might need to be listened too (a primitive becomes a function-local copy)
asyncio.run(ismoke2threads(d))

