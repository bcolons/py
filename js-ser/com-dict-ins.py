class CharNode:
    def __init__(s,ch):
        s.ch=ch
        s.ist =[]
    def __str__(s):
        return s.ch
    def __contains__(s,st):
        out=False
        for elem in s.ist:
            elem.ch==st
            out=True
        return out
    def __index__(s,st):
        ix=-1
        for elem in s.ist:
            ix+=1
            if(elem.ch == st):
                return ix
    def trav(s, words,pre='',ct=0):
        ct=ct+1
        p=s.ch          #1. record child char 
        pre=pre+p       #2. append to prefix 
        words.append("<p>"+"+"*ct+pre)
        if(s.ist):      #3. try to go down
            chit=iter(s.ist)
            while True: # run the iterator till the end
                try:   
                    next(chit).trav(words,pre,ct) # recurse: 1,2,3  
                except StopIteration:
                    break
# cases:
# s.ch==ch && s.list.contains(word[0]) -> s.ist.index(word[0].ins(word[1],word[2:]
# s.ch==ch && s.list.not_contains(word[0]) -> cn=CN(word[0]),s.ist.append(cn), cn.ins(word[1],word[2:])
# s.ch!=ch -> cn=CN(ch),s.append(cn),cn.ins(word[0],word[1:]

    def ins(s,ch,word): # car,cdr or return CharNode(cdr)
        if not word:
            return
        else:
            if s.ch==ch:
                if not s.__contains__(word[0]):
                    print('\nif not s.__contains__(word[0]):'+word[0]+'\n')
                    child=CharNode(word[0])
                    s.ist.append(child)
                    child.ins(word[1],word[2:])
                else:
                    s.ist[s.__index__(word[0])].ins(word[1],word[2:])
            else:
                if not s.__contains__(ch):
                    print('\nif not s.__contains__(ch):' +ch+'\n')
                    child=CharNode(ch)
                    s.ist.append(child)
                    child.ins(word[0],word[1:])
                else:
                    s.ist[s.__index__(word[0])].ins(word[1:])
            return

# ins(word)
# 1. word[0] to s.ch
# 2. s.ist = ins (word[1:] )

#two cases: top root has ch ==''
# A. 1st char is not in a.ist
# construct a CN with s.ch=word[0], set a.list = ins(construct CN with s.ch=word[1])
# B. 1st char is in a.ist
# A. ins(CharNode(word[0],word[1:])
# B. a.ist.index(word[0]).ins(word[1:])

nullroot=CharNode('')
nullroot.ins('r','sabv')
nullroot.ins('z','yxwv')
nullroot.ins('z','yx')
nullroot.ins('r','st')
print('r.sabv\nz.yxwv\nz.yx\nr.st\n')
#s=CharNode('s')

#t=CharNode('t')
#u=CharNode('u')
#v=CharNode('v')
#w=CharNode('w')
#w.ist=[u,v] # w.u, w.v
#s.ist=[t,w] # s.t, s.w, s.wu, s.wv
#r.ist=[s] # r.st, r.sw, r.swu, r.swv
print('should be words, rst, rsw, rswu, rswv, ')

sa=[""]
nullroot.trav(sa)
print(sa)
