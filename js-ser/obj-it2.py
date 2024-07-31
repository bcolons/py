class Ob:
    def __init__(s,ch):
        s.lst=[] # a list of Ob()'s, each must have an s.ch
        s.ch=ch #a char
    def genstr(s,out):
        out+=s.ch
        if(s.lst):
            for elem in s.lst:
                try:
                    next(iter(elem)).genstr(out)
                except StopIteration:
                    out+='...a happy ending!'
                    return out
                except AttributeError:
                    out+="my lit, my lit, my legit lit"
    def __str__(s):
        return s.genstr("")
    def __next__(s):
        return "Next!"
    def __iter__(s):
        return iter(s.lst)
        
a=Ob('y')
b=Ob('z')
e=Ob('x')
b.lst.append(e)
a.lst.append(b)
a.lst.append(e)
d=iter(a)

print('# Output:\n# ----')
print(a)
