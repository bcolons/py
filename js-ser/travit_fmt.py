def trav(recur_iter):
"""traverse any iterator of literal and/or iterables"""

    n=None
    while True: #repeat for each next() until StopIteration raised
        try:
            n = next(recur_iter) #raises StopIteration after last elem
        except StopIteration:
            return 
        try:
            print("n is: "+n) #raises TypeError if n is a (child) iterator
        except TypeError:
            trav(iter(n))  #traverse child iterator

a = {'z':'bb','c':'cc','d':'dd'}
e = [a,'f',(a,'g')]
trav(iter(e))
