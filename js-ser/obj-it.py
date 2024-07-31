class Ob: 
    string_repr=''
    def __init__(s,ch):
        s.ist=[] # a list of Ob()'s, each must have an s.ch
        s.ch=ch #a char
    def genstr(s,out): 
        """ Description: 
                Return a string from traversing a tree of objects.
                Each object has a single data element and an optional list of child objects.
            Implementation: 
                Append data elem's (s.ch) to out. 
                If child list (s.ist) exists: 
                    Iterate over elems checking for and recursively traversing any iterable child objs,
                    StopIteration terminates current iteration,
                        Traversal continues to next elem in parent list.

        """
        out+=s.ch
        if(s.ist):
            chit=iter(s.ist)
            while True:
                try:
                    next(chit).genstr(out)
                except StopIteration:
                    break
    def __str__(s):
        Ob.string_repr=[]
        s.genstr(Ob.string_repr)
        return str(Ob.string_repr)
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
help(Ob.genstr)
print('# a.ist = [Ob-a,[Ob-b,Ob-e],Ob-f,[Ob-g,Ob-h]]')
print('# z.ist = [z,[a,[b,e],f,[g,h]]]')
print('# a.__str__() z.__str__()  is:\n# ----')
print(a)
print(z)
