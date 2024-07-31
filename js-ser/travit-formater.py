import re
def trav(recur_iter,ident=0):
    """traverse any iterator of literal and/or iterables"""
    s="sumstr"
    n=None
    while True: #repeat next() until StopIteration raised then return
        try:
            n = next(recur_iter) #raises StopIteration after last elem
        except StopIteration:
            return 
        if(type(s)!=type(n)): # if not a str (because any str is iterable...)
            try:
                trav(iter(n),ident+1)  #traverse child iterator
            except TypeError: # iter() raised not iterable because it's a literal
                n=str(n)  #toStr any non-str literals
                print("#   |"*ident+"-"+n)
        else:
            print("#   |"*ident+"-"+n)

print("# Output:\n# ----")
a = {'b':'bb','c':'cc',1:'dd'}
e = [a,'f',(a,'g')]
trav(iter(e))
# Output:
# ----
#   |-b
#   |-c
#   |-1
-f
#   |#   |-b
#   |#   |-c
#   |#   |-1
#   |-g
