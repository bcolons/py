import time
class LinkL(): #ordered described as 2prior-impl below
    class Node():
        def __init__(self,key=4,val=2,post=None,prio=None):
            '''Linked list element.
            Contains prior and posterior refs; 'key' is next multiple of prime 'val'
            LinkL initialized to self.head=Node(4 2) start iterator with dispatch(cand=3)'''
            self.post=post
            self.prio=prio
            self.key=key # successively higher multiples of prime, always in order on [n,...,2*n]
            self.val=val # underlying prime
    
        def __lt__(self,a):
            return self.val<a.val
    
        def __str__(self):
            return f'({self.key} {self.val})'

    def __init__(self):
        self.head=self.Node()
        self.tail=self.head # tail is only used to 1 append(..) new and 2 insert(..) existing primes

    def __iter__(self): #iteratively return self.post node
        '''Iterator for linked list, yield each via Node().post refs'''
        cur=self.head
        while cur != None: # cur == None raises StopIteration
            yield cur
            cur=cur.post 
    def __getitem__(self,i):
        '''Iterable for linked list, return ith elem via i iteration Node().post refs (much less efficient than iterator!)'''
        curref=self.head
        cur=0
        while cur < i:  # super inefficient O(n**2) for dump(LinkL)! 'this' ref much?!
            if(not curref.post): raise StopIteration
            cur+=1
            curref=curref.post
        return curref
        
    def search(self,key):
        '''Generic, returns node just beyond key or else None'''
        for elem in self:
            if elem.key > key:
                return elem
        return None

    def match(self,key):
        '''Returns first matching node or None
        As keys are in increasing order, we only need to check the first key in list for a match'''
        return self.head.key == key 
        
    def insert(self,key,val): 
        ''' Generic doub linked list func, must always update 4 refs:
        1 priornode-post and 2 postnode-prior to newnode
        3 newnode-post to postnode
        4 newnode-prior to priornode
        Called only to move(..) head elems (matching multiples) forward in list, append(..) is for new primes'''
        postnode = self.search(key) 
        if(postnode != None): # node should not be inserted as last node
            newnode=self.Node(key,val,post=postnode,prio=postnode.prio) # 3, 4
            postnode.prio.post=newnode # 1
            postnode.prio=newnode # 2 
        else: # append node to end of list
            newnode=self.Node(key,val,post=None,prio=self.tail) # 3, 4
            self.tail.post=newnode #1 , no prior postnode thus 2 does not apply
            self.tail=newnode 

    def move(self,node): # using insert for now.... bc_
        '''Update a node: newkey = oldkey+val (the underlying prime) , 
        Increment a node key by its val, insert 'newnode' to correct new pos
        Free/pop old node from head of list
        '''
        self.insert(node.key+node.val,node.val)
        self.head=self.head.post

    def append(self,key):
        '''Appends a new prime Node, val = prime and key = 2 * prime to end of list'''
        newnode=self.Node(2*key,key,post=None,prio=self.tail)
        self.tail.post=newnode # no prior postnode thus 2 does not apply
        self.tail=newnode 
        
    def dispatch(self,key): # check a new key against list, if match: 1 update-and-forward each match, 2 pop-old match else 3 append new prime
        '''For each matching key (the head)
        1 move entry ahead in list (increment key by one val)
        2 free matching prefixes
        3 If no matches, append new prime as (2 * key, key) to list'''
        matched=False
        while self.match(key):
            matched=True
            self.move(self.head) # pop-free's head 1,2
        if matched == False:
            self.append(key)  # 3
            #print(key) # incrementally output the primes

def dump(iterable):
    '''Helper, calls __str__(elem) for any iterable '''
    for elem in iterable:
        print(str(elem),end='')
    print()

def infini(ct=0): # generator-it.  sadly can't do this with a single line generator-expr [...tho: (x for x in itertools.count() ) ]
    '''Simplest infinite counting integer generator.'''
    while True:
        ct +=1
        yield ct # ie. __next__(): return self.ct+=1

ll=LinkL()
for each in infini(2): # ll is initiallized to (4 2) and we start dispatch(cand=3)
    ll.dispatch(each) 
    dump(ll)    

def add(*a):
    i=0
    print(type(a), a, end=' *a, type .')
    for each in a:
        print(each,type(each),end='(each)') 
        #i=i+each
    return i

def accum(*args,opit,init):     # better is, def accum(itrbl,opit,init):    
    for each in args:
        init = opit((init,each)) #shitty
    return init

def iaccu(iterable,op,init=1): # accum over an iterable for a binary func
    for each in iterable:
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

def filt(stream,pred): # single arg pred
    for each in stream:
        if pred(each):
           yield each

def iseven(inp):
    return True if inp%2==0 else False

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

'''
2 nomat [(4,2)] #1
3 nomat [6,3)(4,2)] #2
4 mat [(6,2)(6,3)]
5 nm [(10,5)(6,2)(6,3)] #3
6 mat [10,5)(9,3)(8,2)]
7 nm [(14 7)(10 5)(9 3)(8 2)] #4
8 m [(16 2)(14 7)(10 2)(10 5)(9 3)]
9 m [(16 2)(14 7)(12 3)(10 2)(10 5)]
10 m [(16 2)(15 5)(14 7)(12 3)(12 2)]
11 nm [(22 11)(16 2)(15 5)(14 7)(12 3)(12 2)] #5
12 m [(22 11)(16 2)(15 5)(15 3)(14 2)(14 7)]
13 nm [(26 13)(22 11)(16 2)(15 5)(15 3)(14 2)(14 7)] #6 suffix has one entry for each prime less than n, prefix does as well (we dont need prefix...)
...
2,3,5,...,Pn-1, n, ... , non-primes greater than n,(and their roots, one entry for each root) ....
lst=filt(infini(0),does_div_fun(3))
print(next(lst))
print(next(lst))
print(next(lst))
#print('nect')
#i= infini()
#print(next(i))
#print(next(i))
#print('mysum infi')
#print(mysum(x) for x in infini(0))
#genin=(mysum(x) for x in infini(0))
#print(next(genin))
#print(next(genin))
#print('listocmp')
#print([mysum(1,2,x) for x in range(3)])
'''
