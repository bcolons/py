class TrNode():
    tntype=type(TrNode("s"))

    def __init__(s,char):
        s.char = char
        s.childTNs = []
    def ins(s, word):
        """word must be an iterator of chars"""
        n=None
        while True:
            try:
                n=next(word)
            except StopIteration:
                return
            tn=TrNode(n)
            if not s.childTNs:
                s.childTNs.append(tn)
                print(n)
            elif s.childTNs.__contains__(tn):
                s.childTNs[s.childTNs.index(n)].ins(word)
            else:
                s.childTNs.append(tn)

     def tntrav(recur_iter,ident=0):
        """traverse any iterator of literal and/or iterables"""
        s=TrNode("sumstr")
        n=None
        while True: #repeat next() until StopIteration raised then return
            try:
                n = next(recur_iter) #raises StopIteration after last elem
            except StopIteration:
                return 
            tntrav(iter(n),ident+1)  #traverse child iterator
            else:
                print("#   |"*iden           print(n)

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

if(__name__=='__main__'):
    r=TrNode("abc")
    r.ins(iter('yiguiopcvbnmlkjh'))
    r.ins(iter('z'))
    r.ins(iter('f'))
    r.ins(iter('4'))
    r.ins(iter('9'))
    r.ins(iter('3'))
    r.ins(iter('7'))
    r.ins(iter('q'))
    r.ins(iter('x'))
