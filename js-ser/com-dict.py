class CharNode:
    def __init__(s,ch):
        s.ch=ch
        s.ist =[]
    def __str__(s):
        return s.ch
    def trav(s, words,prefix=''):
        pre=s.ch
        prefix=prefix+pre
        words.append(prefix)
        if(s.ist):
            chit=iter(s.ist)
            while True:
                try: # try to go down for each elem in this s.ist
                    next(chit).trav(words,prefix) 
                except StopIteration:
                    break

r=CharNode('r')
s=CharNode('s')

t=CharNode('t')
u=CharNode('u')
v=CharNode('v')
w=CharNode('w')
w.ist=[u,v] # w.u, w.v
s.ist=[t,w] # s.t, s.w, s.wu, s.wv
r.ist=[s] # r.st, r.sw, r.swu, r.swv
print('should be words, rst, rsw, rswu, rswv, ')
sa=[""]
r.trav(sa)
print(str(sa))
