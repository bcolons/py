class TrNode():
    def __init__(s,char):
        s.char = char
        s.children = []
    def ins(s, word, child=None):
        n=None
        try:
            n=next(word)
        except StopIteration:
            return
        if not s.children:
            s.children.append(n)
            print('# '+n)
        elif s.children.__contains__(n):
            s.children[s.children.index(n)].ins(word)
            # old meth is: ins(word, s.children[s.children.index(n)])
        else:
            s.children.append(n)
            print('# '+n)
print("# Output:\n# ----")
r=TrNode('a')
r.ins(iter('b'))
r.ins(iter('z'))
r.ins(iter('f'))
r.ins(iter('q'))
r.ins(iter('x'))
            
# Output:
# ----
# b
# z
# f
# q
# x
