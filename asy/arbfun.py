import tracemalloc
def fun1():
    print('fun times one!')
def fun2(inp):
    print('fun times two: ',inp)
def fun3(*inp): # little endian ones tens hundreds etc...
    sofar=0
    power=0
    for each in inp:
        print(each)
        sofar+=int(each)*10^power
        power+=1
    #sofar+=1*int(inp[0])+10*int(inp[1])
    print('infinite fun!: ', sofar)
filt=tracemalloc.Filter(False,tracemalloc.__file__)
tracemalloc.start()

funarr=[fun1,fun2,fun3]
inp=input('enter:\n 1 - fun1(), 2 - fun2(inp) , 3 fun3(*inp):').strip()
snap=tracemalloc.take_snapshot()
if(inp=='1'):
    fun1()
else:
    inp2=input('les args: ').strip()
    if(inp=='2'):
        fun2(inp2)
    else:
        inp3=input('last arg: ').strip()
        fun3(inp2,inp3)
snap2=tracemalloc.take_snapshot()
stats=snap.compare_to(snap2,'lineno')
for each in stats:
    print(each)
