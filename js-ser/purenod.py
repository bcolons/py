class PureNod:
    ct=0
    def __init__(s):
        s.arr=[]
        s.ct=PureNod.ct
        PureNod.ct+=1
    def genstr(s,stbuf=[]):
        stbuf.append(str(s.ct)+',')
        for elem in s.arr:
            try:
                elem.genstr(stbuf)
            except StopIteration:
                pass
        return stbuf
    def __str__(s):
        return str(s.genstr())
        
    def __str__(s):
        return str(s.genstr())
    def ins(s,inp):
        pass
a=PureNod()
b=PureNod()
c=PureNod()
d=PureNod()
e=PureNod()
f=PureNod()
g=PureNod()
c.arr =[a,b]
d.arr=[e,f]
g.arr=[c,d]
#
#         g6 -> g.arr = [c,d]
#        /  \
#       /    \
#      c2     d3 -> d.arr =[e,f]
#     / \    / \
#    a0  b1 e4  f5 -> f.arr =[]

print('# '+str(g))
# Output:
# ['6,', '2,', '0,', '1,', '3,', '4,', '5,']
