class StrBuf:
    def __init__(s):
        s.st=''
    def __add__(s,t):
        s.st=s.st+t
        return s
    def __str__(s):
        return str(s.st)
class StrArr:
    def __init__(s):
        s.sa=[]
    def __str__(s):
        return str(s.sa)
    def append(s,t):
        s.sa.append(str(t))
        return

class Ob: 
    def __init__(s,ch):
        s.ist=[] # a list of Ob()'s, each must have an s.ch
        s.ch=ch #a char
    def genstr(s,out): 
        """ Description: 
                Return a string from each path down a tree of objects.
                Each object has a single char element and an optional list of child objects.
            Implementation: 
                Append data elem's (s.ch) to build a prefix string
                If child list (s.ist) exists: 
                    Iterate over elems checking for and recursively traversing any iterable child objs,
                    StopIteration writes current prefix to output StrArr
                        Traversal continues to next elem in parent list with parent prefix.

        """
        print('partial prefix: '+out)
        out+=s.ch
        if(s.ist):
            chit=iter(s.ist)
            while True:
                try:
                    next(chit).genstr(out)
                except StopIteration:
                    print('StIt: '+out)
                    break
        else:
            print('No Child: '+out)
    def __str__(s):
        return str(s.genstr(""))
    def __next__(s):
        return "Next!"
    def __iter__(s):
        return iter(s.ist)
        
a=Ob('a')
b=Ob('b')
e=Ob('e')
f=Ob('f')
gh=Ob('g')
gh.ist.append(Ob('h'))
b.ist.append(e)
a.ist.append(b)
a.ist.append(f)
a.ist.append(gh) 
# a.ist = [Ob-a,[Ob-b,Ob-e],Ob-f,[Ob-g,Ob-h]]
z=Ob('z')
z.ist.append(a)
# z.ist = [z,[a,[b,e],f,[g,h]]]
print('# a.ist = [Ob-a,[Ob-b,Ob-e],Ob-f,[Ob-g,Ob-h]]')
print('# z.ist = [z,[a,[b,e],f,[g,h]]]')
print('# a.__str__() z.__str__()  is:\n# ----')
print('a is: '+str(a))
print('z is: '+str(z))

s1=StrBuf()
s1=s1+'w'
s2=s1+'x'
print(type(s1))
print(s2)
