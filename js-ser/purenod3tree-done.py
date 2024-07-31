class PureNod:
    ct=0
    def __init__(s):
        s.arr=[]
        s.ct=PureNod.ct
        PureNod.ct+=1
    def genstr(s,stbuf=[]):
        stbuf.append(str(s.ct)+',')
        for elem in s.arr:
            elem.genstr(stbuf) 
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
h=PureNod()
i=PureNod()
d.arr =[a,b,c]
h.arr=[e,f,g]
i.arr=[d,h]
#
#         i8 
#        /  \
#       /    \
#      /      \
#     /        \
#    /          \
#   d3          h7
#  /| \        /| \
# / |  \      / |  \
#a0 b1 c2   e4  f5  g6

print('# '+str(i))
# Output:
# ['8,', '3,', '0,', '1,', '2,', '7,', '4,', '5,', '6,']
