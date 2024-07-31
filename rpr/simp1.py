''' Recursively turn a string into a python list; and then other way 'the Dual' (ignoring malformed/exceptions/etc)'''
a_st='ab[cd]ef[ghi]j' # a_py =['a','b',['c','d'],'e','f',['g','h','i'],'j']
a_stmixed='ab[c{mi[dd]le}d]ef[ghi]j'

def splitch(chpat,termchar=None,lstit=iter(),out=[],elem=[]):
    '''Return a list of strings for input iter delimited by chpat. 
    General use for both [..,..,..] and {..:..,..:..,..} strings; chpat in { [ , :'''
    try:
        n=next(lstit)
        if n=='chpat': return  out.append(elem) # inp elem is consumed, 
        else: splitch(chpat,lstit,out,elem.append(n) # elem is one char longer
    except StopIteration: return out # input list is consumed
        

def parse(stit):
    'Parse char strings with nested [..] containers'
    out=[]
    try:
        while True:
            n=next(stit)
            if n=='[': out.append(parse(stit)) #down
            elif n==']': return out #up
            else: out.append(n) #across
    except StopIteration: #end of input iterator reached
        return out
print(parse(iter(a_st)))


def parse_mix(stit,closechar=']'):
    'bc_ broken because set not nestable/hashable....Parse char strings with nested {..} and [..] containers'
    outl=[]
    outs=set()
    retcont={']':outl,'}':outs}
    retfunc={']':outl.append,'}':outs.add}
    try:
        while True:
            n=next(stit)
            if n=='[': outl.append(parse_mix(stit,']')) #down into new list
            elif n=='{': outs.add(parse_mix(stit,'}')) #down into new set
            elif n==closechar: return retcont[closechar] #up closing existing list or set
            else: retfunc[closechar](n) #across add/append elem
    except StopIteration: #end of input iterator reached
        return outl #toplevel is list
#broken print(parse_mix(iter(a_stmixed)))

def parse_mixd(stit,closechar=']'):
    'Parse char strings with nested dict {..} and list [..] containers'
    outl=[]
    outs=dicte()
    retcont={']':outl,'}':outs}
    retfunc={']':outl.append,'}':tupluseq}
    try:
        while True:
            n=next(stit)
            if n=='[': outl.append(parse_mixd(stit,']')) #down into new list
            elif n=='{': 
                outs=outs+parse_mixd(stit,'}') #down into new set
            elif n==closechar: return retcont[closechar] #up closing existing list or set
            else: retfunc[closechar](n) #across add/append elem
    except StopIteration: #end of input iterator reached
        return outl #toplevel is list
def incdc(stit,dc):
    'Add elems incrementally to a dict; halt upon } char'
    try:
        n=next(stin)
        if n == '}': return dc
        elif key == None: incdc(stit,dc,key=n)
        else: 
def inclt(stit,lt):
    'Add elems incrementally to a list: halt upon ] char'
    try:
        n=next(stin)
        if n==']': return lt
        else

print(parse_mix(iter(a_stmixed)))
