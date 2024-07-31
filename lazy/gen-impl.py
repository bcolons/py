import time
class LinkL(): #ordered described as 2prior-impl below
    class Node():
        def __init__(self,mult=4,prim=2,post=None,prio=None):
            '''Linked list element.
            Contains prior and posterior refs; 'mult' is next multiple of prime 'prim' '''
            self.post=post
            self.prio=prio
            self.mult=mult # successively higher multiples of prime, always in order on [n,...,2*(n-1th.prim) or 2*n-2th.etc.. or other]
            self.prim=prim # underlying prime
    
        def __lt__(self,a):
            return self.prim<a.prim
    
        def __str__(self):
            return f'({self.mult} {self.prim})'

    def __init__(self):
        self.head=self.Node()
        self.tail=self.head # tail is only used to 1 append new and 2 insert(..) existing primes if past end of list

    def r_getitem__(self,i):
        print(self.head)
        curref=self.head
        cur=0
        while cur < i and curref.post !=None: 
            #print(curref)
            cur+=1
            curref=curref.post
        return curref

    def __iter__(self): #iteratively return self.post node
        '''Iterate through linked list via Node().post refs'''
        cur=self.head
        while cur != None: # cur == None raises StopIteration
            yield cur
            cur=cur.post 
        
    def search(self,mult):
        '''Generic, returns node just beyond mult or else None'''
        for elem in self:
            if elem.mult > mult:
                return elem
        return None 
    def match(self,cand):
        '''Returns True if candidate matches next node; else False
        (As mults are in increasing order all greater or equal to cand, we only need to check the first mult) '''
        return self.head.mult == cand 
        
    def insert(self,mult,prim): 
        ''' Generic doub linked list func, if added to constructor...more garbage
        Must always update 4 refs:
        1 priornode-post and 2 postnode-prior to newnode
        3 newnode-post to postnode
        4 newnode-prior to priornode
        Called only to move(..) head elems (matching multiples) forward in list, append(..) is for new primes'''
        postnode = self.search(mult) 
        if(postnode != None): # special steps if node inserted at end
            newnode=self.Node(mult,prim,post=postnode,prio=postnode.prio) # 3, 4
            postnode.prio.post=newnode # 1
            postnode.prio=newnode # 2 
        else:  # happens twice when 3 and 7 are largest primes, multiples 6 and 15 land past end of list..oh well
            newnode=self.Node(mult,prim,post=None,prio=self.tail) # 3, 4
            self.tail.post=newnode #1 , no prior postnode thus 2 does not apply
            self.tail=newnode 

    def move(self,node): # using insert for now, more self-garbage.... bc_
        '''Update a node: newmult = oldmult+prim (the underlying prime) , 
        Increment a node mult by its prim, insert 'newnode' to correct new pos
        Free/pop old node from head of list
        '''
        self.insert(node.mult+node.prim,node.prim)
        self.head=self.head.post

    def dispatch(self,cand): # check a new candidate against list, if match: 1 update, move each match; 2 pop-old match; else: 3 append new prime
        '''For each matching mult (the head) 
        1 move entry ahead in list (increment mult by one prim)
        2 free matching prefixes
        3 If no matches, append as new prime as (2 * prim, prim) to list
        concise and efficient impl for while-else logic 'while mult match(cand): move; else: append as prim=cand)' '''
        if not self.match(cand):    # 3 prime-case, append Node
            newnode=self.Node(mult=2*cand,prim=cand,post=None,prio=self.tail)
            self.tail.post=newnode
            self.tail=newnode 
        else:                       # 1,2 one or more heads match/is a multiple
            self.move(self.head)
            while self.match(cand): self.move(self.head) # must move one Node for each unique prime factor for cand

def dump(iterable):
    '''Helper, calls __str__(elem) for any iterable '''
    for elem in iterable:
        print(str(elem),end='')
    print()

def dumpr(itrbl):
    it=iter(itrbl)
    try:
        print(str(next(it)),end='')
        dumpr(it)
    except StopIteration:
        print()
print('dumpr')
dumpr((1,2,3,4,9))
dump((1,2,3,4,9))
def count_up_to(bound=False):
    ct=0
    while bound==False or ct < bound :
         ct+=1
         yield ct

#for e in count_up_to():
    #print(e)

def infini(ct=0): # generator-it.  sadly can't do this with a single line generator-expr [...tho: (x for x in itertools.count() ) ]
    '''Simplest ascending integer generator.    
    Trivial templ for __iter__(..) that keeps yielding'''
    while True:
        ct +=1
        yield ct # ie. __next__(): return self.ct+=1

def infct(ct=0):
    def inner():
        nonlocal ct # req'd
        ct+=1
        return ct
    return inner
i=infct(9)
i()
i()
i()
print('4th call(ct=9):',i())
def infinf1():
    while True:
        yield lambda: 1

def addinf(itrbl): # template for building recursive func(iterable) bc_ doesnt work...never yields anything, then returns
    a=iter(itrbl)
    try:
        yield next(a)+addinf(a)
    except StopIteration:
        pass

def bc_nextr(itrbl):# func(itrbl) and returns generator, simple/generic template
    it=iter(itrbl)
    running=0
    while True:
        try:
            running+=next(it)
            yield running
        except StopIteration:
            return
''' iterable is the common interface 'for...in itrbl:' which loops over:
generator func [f(.): while: yield; else return] 
generator exp (f1,f2,...)
iterator [iter(some sequence objects (or funcs--tho must call() these))]'''

def bc_gentr(genrbl,func): # generator in, generator out
    for yielded in genrbl:
        yield func(yielded)

def times10(arg): return arg * 10

def echo_iter(itrbl):
    for yielded in iter(itrbl):
        yield yielded 
print('bc_n')
for addi in bc_gentr(bc_nextr(((2,4,6))),times10):
    print(addi)

ll=LinkL()
for each in infini(2):
    #print(each,end='')
    ll.dispatch(each) 
    #dump(ll) #dump ll each new input

def add(*a):
    i=0
    print(type(a), a, end=' *a, type .')
    for each in a:
        print(each,type(each),end='(each)') 
        #i=i+each
    return i

def accum(*args,op,init):     # better is, def accum(itrbl,op,init):    
    for each in args:
        init = op((init,each)) #shitty
    return init

def accum_it(itrbl,op=None,lval=None): #binary func(x,y) requires to lookahead that y exists/is valid...not easy to do recursive iteration
    '''correct except returns last elem operated on twice....'''
    it=iter(itrbl)
    try:
        lval=next(it)
        return op(lval,accum_it(it,op=op,lval=lval))
    except StopIteration:
        return lval # requires a meaningful or correct op(nullval,...)=nullval...still call op that last pointless time

def accum_it2(itrbl,op=None,lval=None,rval=None): #binary func(x,y) requires to lookahead that y exists/is valid...not easy to do recursive iteration
    '''delays op(..) until both operands exist/are-valid''' # bc_ notworking
    it=iter(itrbl)
    lval=rval
    try:
        rval=next(it)
        return op(lval,accum_it(it,op=op,lval=lval))
    except StopIteration:
        return nval # requires a meaningful or correct op(nullval,...)=nullval...still call op that last pointless time
    
def iaccu(iterable,op,init=1): # accum over an iterable for a binary func(x,y) for each in iterable:
    for each in iter(iterable):
        init=op(init,each)
    return init

def mul2(a,b): # binary mul
    return a*b
def imul(iterable): # iterable ver from binary mul2
    return iaccu(iterable,mul2,init=1)

def add2(a,b): # binary add
    #return a.__add__(b)
    return a+b
def iadd(iterable): # iterable ver from binary add2
    return iaccu(iterable,add2,init=0)

#print(accum_it((0,1,2,3),op=add2))
#print(accum(0,1,2,3,opit=iadd,init=0))
#print(accum(1,2,3,4,opit=imul,init=1))
#print(accum(1,2,3,4,opit=iadd,init=0))
#print(iaccu((1,2,3,4.1),op=add2,init=0))
#print(iaccu((1,2,3,4),op=int.__add__,init=0))

def mysum(*args,sum=0,delay=.1):
    for each in args:
        time.sleep(delay)
        sum+=each
        print(f'{each}:{sum}:{time.time()}')
    return sum

def filt(itrbl,pred): # single arg pred
    it=iter(itrbl)
    for each in it:
        if pred(each):
           yield each
def filtr(itrbl,pred): # doesnt work bc_ , loop unrolling  plus recursion is messy
    it=iter(itrbl)
    out=[]
    try: 
        n=next(it)
        if pred(n): return out.append(n).append(filtr(it,pred)) 
        else: return out.append(filtr(it,pred))
    except BaseException as e: print(e)

def filts(itrbl,pred,endtok=None):
    it=iter(itrbl)
    def inner():
        try:
            n=next(it)
            while not pred(n): n=next(it)
            return n
        except StopIteration as e: return endtok # runtime exception does not a generator make, yield does
    return inner

def iseven(inp):
    return True if inp%2==0 else False

def itrbl_now(delay_itrbl): 
    ''' Alternative to generator-yield-next...
    first invc returns a func with state...
    sbsq calls return iterations/return vals
    Cant really interface with; for...in itrbl: as StopIteration isnt caught.... 
    Generator func must actually 'yield', or else eventually (perhaps) fall through and return
    Exception is any infinite 'nexterator' generator func where next(.) always succeeds, although still cant be use in; for...in itrbl: '''
    def nexterable():
        return next(delay_itrbl)+time.time() 
    return nexterable # lazy, only eval'd at nexterable() call

def itrbl_now_canon(delay_itrbl): # the right way
    for yielded in delay_itrbl:
        yield yielded+time.time()

n=itrbl_now_canon(iter((2,2))) # the right way
for each in n:
    time.sleep(1)
    print(each)

n=itrbl_now(infini(2)) # the exception where some 1 infinite generator func 2 input to nexterator may be 3 looped with; for...in itrbl: bc_ so rare!
def to_iterable(nfunc): 
    '''Nexterator to an iterable which may be used in: for yielded_or_nexted in iterable: '''
    print(nfunc,'nfunc')
    while True:
        yield nfunc()

for each in to_iterable(n): 
    print(each)

def now(delay): 
    '''Encapsulate args to an arg-less inner 'nexterator'
     sbsq calls work just like next(generator) until None or other terminator'''
    def nexterator():
        return delay+time.time()
    return nexterator

n=now(delay=2)
while (each:=n()) != None: # nexterate! cleaner is: for yielded in iterable: (but less fun)
    pass #print(each)
#prin=filt((1,2,3,4,5,6),iseven)
#for e in prin:
    #print(e)
print('filtr')
#prin=filts((1,2,3,4,5,6),iseven)
#for e in prin:
    #try:
        #print(next(e))
    #except:
        #print(e)
def inc(a):
    return lambda : inc(a+1)
res=inc(9)
print(res(),res()())
def does_div_fun(base): 
    '''Returns a f(arg) where base divides arg? (True or False) '''
    return lambda arg: True if arg % base==0 else False

def does_div_gen(base=0):
    while True:
        base+=1
        yield does_div_fun(base)

# two diff approaches: 
# 1now DIVIDE find remainder for each prime 2,...,sqrt(n)  # shitty division, most concise though ...
# 2prior MULTIPLY all primes < n-1  (Actually add! ..int-add probably slower than mult, smaller mem footprint tho...)
# tuples of [(prime,next_multiple),...] sorted by multiples for each prime < n, if n not in list its prime
# if any next_multiple == n; update it/them to next_multiple+=prime and insert correctly into sorted list)
# ...naively impl; then try later with streams
