import inspect
import re
import sys
import asyncio 
import time
import tracemalloc

class C:
    def __init__(self):
        self.d=0
        self.die=False
    def inc(self):  
        self.d+=1
        return self.d
    def plus(self,*nums):
        for each in nums:
            self.d+=nums
    def main(self): 
        while self.die != True: # main thread will complete
            time.sleep(1)
            self.inc()
    def kill(self):
        self.die=True
def listen(obj,tty='/dev/tty2'):
    '''Method to discover and call methods on an object via tty2 by default, 
    while obj.main() lives and runs in another thread.
    '''
    with (
        open(tty,'r') as lfdi, 
        open(tty,'w') as lfdo, ):
        mems={}
        arr=enumerate(inspect.getmembers(obj))
        for each in arr: # populate dict with A-Za-z keys
            mems[achr(each[0])]=each[1]
        
        while True:
            inp=lfdi.read(1)
            if False:
                pass
            elif inp == 'z': # dump char-keyed list of members for obj
                arr=enumerate(inspect.getmembers(obj))
                for each in arr: # populate dict with A-Za-z keys
                    mems[achr(each[0])]=each[1]
                for each in mems: # dump all keys/vals 
                    lfdo.write(f'{each} - {mems[each]}\n')
                lfdo.flush()
            elif inp =='y': # kill main() and listen() loops
                obj.kill() # 'kills' the main() thread: exits loop, completes
                break # 'kills' the listen thread: exits loop, completes
            elif inp =='x': # enter a char-key to call a zero-arg method
                inp=lfdi.read(1)
                #lfdo.write(str(eval('obj.inc()'))) # lfdi.read(3)))) ...works.
                try:
                    f=mems[inp] # 2-tuple with char-selected (method name, bound method)
                except KeyError:
                    f=mems['c'] #inc() ...just so something observable happens
                lfdo.write(str(f))
                lfdo.write(str(f[1]()))
                lfdo.flush()
            elif inp =='w': # enter a char-key to return cur value of data member, else will give string versions of methods, or KeyError
                inp=lfdi.read(1)
                mem1=None
                try:
                    mem1=mems[inp] # tuple with char-selected bound method
                except KeyError:
                    mem1=mems['a'] #self.d ...just so something observable happens for a data member
                lfdo.write(str((mem1[0],obj.__getattribute__(mem1[0]))))
                lfdo.flush()
            elif inp =='v': # enter a char-key for a method then args + \n, doesnt work...
                inp=lfdi.read(1) # user enters char for a single-arg method
                mem1=mems[inp] # set bound func, exception unless key exists
                inparg=lfdi.readline().strip() # user enters func arg plus two \n 's
                lfdo.write(str(mem1[1](int(inparg))))
                lfdo.flush()
            elif inp =='u': #enter a line of input + \n , will echo input
                inp=lfdi.readline() # actually readline()  hangs after the first \n ... so do it twice?
                lfdo.write(str(inp)) 
                lfdo.flush()
            elif inp =='t': # single-arg method-case, doesnt work...more complicated than single threaded ref case....
                inp=lfdi.read(1)
                mem1=mems[inp][1]
                lfdo.write('enter integer for arg to '+str(mem1)+'\n')
                lfdo.flush()
                inparg=lfdi.readline().strip() # tuple of args
                lfdo.write(mem1(str(inparg)))
                lfdo.flush()
                #mem1(inparg)
                #unpack(mem1,inparg)
                #lfdo.write(str(
                #lfdo.flush()
            else:
                pass # newlines all other chars do nothing 
def unpack(f,*args):
    return f(args)
def aord(inp): 
    '''alphabet-ord(): Map A-Za-z codes 65-90,97-122 onto 0-25,26-51 '''
    o=ord(inp)
    if o < 91:
        return o - 65 # gives 0 for A, 1 for B, etc...
    else:   
        return o - 71  # gives 26 for a,97; 27 for b,98; 51 for z,122
def achr(inp):
    '''alphabet-chr(): Map 0-25,26-51 onto A-Za-z codes 65-90,97-122'''
    if inp < 26:
        return chr(inp+65) # gives A,65 for 0; B for 1 ... Z,90 for 25
    else:
        return chr(inp+71) # gives a,97 for 26; b,98 for 27 ... z,122 for 51
def arange(len):
    outp=[]
    for elem in range(len):
        outp.append(achr(elem))

def grep(pat):
    with open(sys.argv[0],'r') as src:
        r=re.compile(pat)
        while(line:=src.readline()):
            if(None!=re.search(r,line)):
                print(line)

async def runmain():
    '''Simplest system to run an object's main() in one thread and see and call object's methods in another listen-thread.'''
    c=C()
    try:
        grep('elif')
    except TypeError as t:
        print("grep() typeerr'd :"+str(t))
    await asyncio.gather(
        asyncio.to_thread(c.main), 
        asyncio.to_thread(listen(c)),)
#tracemalloc.start()
try:
    asyncio.run(runmain())
except TypeError:
    print('TypeError - asyncio.run doesnt know what to do with a NoneType')

#snapshot = tracemalloc.take_snapshot()

#stats=snapshot.statistics('lineno')
#for each in stats:
#    print(each)
    
    
   
    
    
    
