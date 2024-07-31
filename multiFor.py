def ret(a): # simplest func
    return a

def ret_list(a=[]):
    for elem in a: 
        return a

def print_simp_loop(a):
    for elem in a:
        print(elem)
def print_loop(list_a,listfunc=ret,elemfunc=ret): 
    '''Print elemfunc(elem) for each elem in listfunc(list_a)
    list_a - list of input values
    listfunc - callable that takes a single list of values
    elemfunc - callable that takes a single scalar value'''
    for elem in listfunc(list_a):
        print(elemfunc(elem))
def add(*args):
    '''Unpack and add an arbitrary n-tuple of args.'''
    mysum=0
    print(type(args))
    for arg in enumerate(args):
        print(type(arg))
        mysum+=arg[1]
    return mysum

def add_ab(a,b):
    return a+b

def unpack_add(arg): 
    '''Unpack a 2-d arg tuple and call add_ab()'''
    return add_ab(*arg)
def nunpack_add(arg):
    return add(*arg)
def sq(a):
    return a*a

a=[1,2,3,4]
b=[10,20,30,40]
print(add((2,3,3,3,3,3,3,99))) #do need double parens, the tuple-izer...
print(nunpack_add((2,3,3,3,3,3,3,99)))
print(unpack_add((2,3)))

for xy in (a,b): # same as: for xy in a,b:
    print(xy[1]+xy[0])

#output
# 3 # a[0]+a[1]
# 30 # b[0]+b[1] 

for xy in zip(a,b):  # multifor !
    print(xy[1]+xy[0])
#output
# 11,22,33,44

print_loop(([xy[0]+xy[1] for xy in zip(a,b)]),ret,ret) # 2-d list comp
print_simp_loop([xy[0]+xy[1] for xy in zip(a,b)]) # 2-d list comp
#also
print_loop(a,ret,sq)
