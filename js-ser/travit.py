def trav(recur_iter):
    """traverse any iterator of strings and/or iterables"""

    n=None
    while True: #repeat for each next() until StopIteration raised
        try:
            n = next(recur_iter) #raises StopIteration after last elem
        except StopIteration:
            return 
        try:
            print(""+n,end='') #raises TypeError if n is a (child) iterator
        except TypeError:
            trav(iter(n))  #traverse child iterator

def trav2(recur_iter):
    """Equivalent but more pythonic traverse any iterator of literal strings and/or iterables"""

    for n in recur_iter:
        if(type(n) is not type(123)):
            trav2(n)
        else:
            print(n,end='')   
def travgen(recur_iter):
    """Generator traversal of iterator of literal numbers and/or iterables"""
    for n in recur_iter:
        if(type(n) is not type(123)):
                print('for n... in recur_iter '+str(type(n)))
                travgen(n)
        else:
            yield n
        
#e=['z','a',['b','c'],['d',['e','f']]]
e=[1,2,[3,4],[5,6],7]
#a = {'z':'bb','c':'cc','d':'dd'}
#e = [a,'f',(a,'g')]

#print("trav():     ",end='')
#trav(iter(e))

print('\ntrav2():    ',end='')
trav2(iter(e))

print('\ntravegen(): ',end='')
for i in travgen(e):
    print( i, end='')

myit=travgen(iter(e))
#while(True):
    #i=input('enter nothing...')
#    print(next(myit))
# Output:
# ----
# n is: z
# n is: c
# n is: d
# n is: f
# n is: z
# n is: c
# n is: d
# n is: g
