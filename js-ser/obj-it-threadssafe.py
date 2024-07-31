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
    def __add__(s,t):
        s.sa.append(str(t))
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
                Return a string from traversing a tree of objects.
                Each object has a single data element and an optional list of child objects.
            Implementation: 
                Append data elem's (s.ch) to class string out. 
                If child list (s.ist) exists: 
                    Iterate over elems checking for and recursively traversing any iterable child objs,
                    StopIteration terminates current iteration,
                        Traversal continues to next elem in parent list.

        """
        out.append(s.ch)
        if(s.ist):
            chit=iter(s.ist)
            while True: #iterate through Ob's in chit
                try:
                    next(chit).genstr(out)
                except StopIteration:
                    break
    def __str__(s):
        o=StrArr()
        s.genstr(o)
        return str(o)
    def __next__(s):
        return "Next!"
    def __iter__(s):
        return iter(s.ist)
        
# genstr(app,out=="") # s.ist=[bat,fig,gig]
# out.append('a')
#  genstr(bat) # s.ist= [egg]
#  out.append('b')
#   genstr(egg) # s.ist=None
#   out('e')
#   StopIt
#  genstr(fig) # s.ist=None
#  out('f')
#  StIt
# genstr(gig) # s.ist=None
# out('g')
#  genstr(Ob('h')) # s.ist=None
#  StIt
#...completes
app=Ob('a')
bat=Ob('b')
egg=Ob('e')
fig=Ob('f')
gig=Ob('g')
gig.ist.append(Ob('h')) # hat
bat.ist.append(egg) # bat.ist -> [egg]
app.ist.append(bat) # app.ist -> [bat -> [egg]]
app.ist.append(fig) # app.ist -> [bat -> [egg], fig]
app.ist.append(gig)  # app.ist -> [bat -> egg], fig, gig]
zeb=Ob('z')
zeb.ist.append(app)
for el in app.ist:
    print('app-elem is: '+el.ch)
for el in zeb.ist:
    print('zeb-elem is: '+el.ch)
print("# app.ist -> [bat -> egg], fig, gig -> Ob('h')]")
print("# zeb.ist -> [app -> [bat -> egg], fig, gig -> Ob('h')]")
print('# a.__str__() z.__str__()  is:\n# ----')
print('str-app is: '+str(app))
print('str-zeb is: '+str(zeb))
