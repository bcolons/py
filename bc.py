import inspect
import doctest
import re

def ppp_s(obj='teststring....[{(4,5,6),(7,8),{a,b},},abf]',ind=0,): # like with inspect.getmembers(..) as [(input attr_name, attr_val
    '''simply __str__() an open-close-char nested string strings, use newline-then-python-pretty-printing to show inner/contained collections....
    Function creates a prototype of output for ppp and variants which traverse down via contained objects and/or nested collections'''
    open_pat=re.compile('\{|\[|\(') # fixme, shouldnt count when within str
    close_pat=re.compile('\}|\]|\)') # fixme, shouldnt count when within str
    ind=0
    print(inspect.stack())
    for each in str(obj):
        if open_pat.search(each):
            ind+=1
            print('\n',' '*4*ind,end='') 
        elif(close_pat.search(each)):
            ind-=1      
        print(each,end='')
    print()
     
def ppp(obj,ind=0):
    ''' python-pretty-print, display an object's members, space-indenting when descending into contained objects.
    Formatting mostly mimics the default __str__ format for non-primitives (and in fact uses print(..) prior to descending).
    Collections are displayed twice, __str__() and then per-element.
    More generally useful logic divides the dataverse (new word!!!) into: 
        1. primitive(i,bool,f,str)
        2. non-dict container (list,set,tuple, ...star-iterators pointing to any of 1.-4.)
        3. dict container
        4. object (here is a special case of 3. so we sbst obj.__dict__ )
    '''
    if(isprm(obj)):
        print(' '*4*ind,type(obj),obj)
    elif(isdct(obj)):
        ppp_dct(obj,ind+1)
    elif(isobj(obj)):
        ppp_dct(obj.__dict__,ind+1)
    else:
        try: # is iterable ? pprettyp each one...except when not, print single one 
            for each in obj:
                ppp(each,ind+1)
        except BaseException:
            print(' '*4*ind+' t: ',type(obj),' o: ',obj)

def pppt(obj,ind=0):
    '''Ppprint what you have, recursive-descend into any dict/obj/iterable.'''
    print(' '*4*ind+' t: ',type(obj),' o: ',obj) # main output, nested data is sbsq ppp(..)'d 
    if(isdct(obj)): # special case num1, fixme: keys are allowed to be any hashable, bc_ here only primitives
        for eachkey in dct:
            pppt(dct[eachkey],ind+1) # again we leave the keys un-descended
    elif(isobj(obj)): # special case num2
        pppt(obj.__dict__,ind+1)
    elif(not isstr(obj)): # str is iterable but not what we want to do here
        try: # is iterable ? pprettyp each one.
            for each in obj:
                pppt(each,ind+1)
        except BaseException:
            print(' WTF??? '*4*ind,type(obj),obj) # identify the ones that escape classification....

def ppp_dct(dct,ind):
    for eachkey in dct:
        ppp(dct[eachkey],ind)

def ppp_con(con,ind):
    try:
        for each in con:
            ppp(each,ind)
    except BaseException:
           pass
    
def isstr(inp):
    return isinstance(inp,str)
def isprm(inp): # four that i can think of 
     return isinstance(inp,int) or isinstance(inp,bool) or isinstance(inp,float) or isinstance(inp,str)
def isprmu(inp):
    return (inp == (int | float | str))
def isdct(inp): # the one, the only....
    return isinstance(inp,dict)
def isobj(inp): # silly test but not sure how else to do it
    try:
       return inp.__dict__==inp.__dict__ 
    except AttributeError:
        return False

def ppp_short(obj,ind=0): # way shittier to read, only should use try-catch as a last resort as above: isobj()
    print(' '*4*ind,obj)
    try:
       obj=obj.__dict__ # is an object
    except AttributeError: # not an object, doesnt have a __dict__
        try: 
            for each in obj: # prim raises not-iterable, any object is now obj.__dict__
                try:
                    ppp_short(obj[each],ind+1) # is an object.__dict__ or a dict 
                except TypeError: # not subscriptable BUG HERE: for lst=[1,2,3] for i in lst: lst[i] works but is wrong, checking types is much better
                    ppp_short(each,ind+1) #covers the rest
        except ValueError: # not iterable or obj
            pass # already printed primitive, cast obj to obj.__dict__
        
def mem(obj):
    return inspect.getmembers(obj)
class O:
    #def __init__(self):
        #self.omem='Omember data'
    def ometh():
        return 1
class P(O):
    def pmeth():
        self.pmem='P member data'

if(__name__=='__main__'):
    #quick brown fox
    a = ['q','uic',[' ','br'],'own ',['f','ox']]
    ppp(a)
    o=O()
    p=O()

    pppt(mem(p))
    print(mem(p))

    '''recurd={'a':{'aa':'lava','ab':'testing'}:'b':{'ba':'blacksheep','bc':'thatsme'},'c'

    obj.dct -> {(lit:lit|obj|dct)*}
    stepwise cases:
    obj.dct -> {lit:lit} # covered by print(..)/repr(..)
    obj.dct -> {(lit:obj} # covered by print(lit)
    obj.dct -> {(lit:lit|obj|dct)*}
    '''

