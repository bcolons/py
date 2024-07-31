import re
'''
    (De)Serialize python members as json-esque objects, arrays and literals ie. nested containers [..] and { .. : ..}
    Single pass in both 1.write/store and 2.read/load directions: (for simplicity and possibly infinite input)
    1A. write container chars and literal elems as python tree traversed
    2A. lex container tokens 2B. parse-to-tree 
    [ - new list, .append(rest of list), return upon ] 
    { - new dict, .add(rest of key/val's), return upon } 
    ...later commas and ...later semi-colons
    '''

tok={'[':']','{':'}'} # tok['{'] == '}' 

def walkstring(stiter, tok, func=str):
    'apply condition to each in stin, once True return func(restofstring))'
    out=[]
    n=''
    while True:
        try :
            n=next(stiter)
            if n==tok['['] : # descend down a branch of tree, common to { and [
                out.append(walkstring(stiter,up_down_ntkens[dhar])) #just skips the char, varies acc to { or [
            else: #traverse across a branch of tree 
                out.append(n)
        except StopIteration:
            return out #ascend from an exhausted branch

def rper(o):
    'Serialize-with-type-hint any member/composite primitive obj: rper(obj)'
    #primitive atoms
    sp=re.compile('str')
    ip=re.compile('int')
    fp=re.compile('float')
    bp=re.compile('bool')
    #builtin containers, inverse of repr(container)
    lp=re.compile('list') #already json 'array'. [elem1, elem2...]  as ['list',elem1,elem2,...]
    tp=re.compile('tuple') #immut (elem1, elem2, ...) as json ['tuple',elem1,...]
    sp=re.compile('set') #incl frozenset,{elem1, elem2, ...} as json ['set'|'froz',elem1,...]
    dp=re.compile('dict') #already json 'object', {'type':'dict',key1:val1,key2:val2,...} 

    #builtin container types: recur? length-based? (notpythonic)

    #cp=re.compile('type')
    #op=re.compile('object')
    if sp.search(o[0]):
        return o[1] # already an inst of str
    elif ip.search(o[0]):
        return int(o[1])
    elif fp.search(o[0]):
        return float(o[1])
    elif bp.search(o[0]):
        return bool(o[1])
    elif bp.search(o[0]):
        return bool(o[1])
    else: return o #why not

def rpr(o):
    return (repr(type(o)),repr(o))

stuff=[1,'2',{3.3:False}]
for each in stuff:
    print(f'{rpr(each)} {rper(rpr(each))}')
    

print(walkstring(iter('abcdefghi'),'d',repr))

