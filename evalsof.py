def eval_until_close(strit,sofar=''):
    '''ExmpA Return result of parenthically nested, evaluat-able stuff (python exprs, outermost needs outer parens)
    Simplest example of no-assignment, recursive generate-then-(eval)-traverse a tree generated from a string'''
    try:
        n=next(strit) # n is in three cases down, across, up
        print(f'{n} in n')
        if n=='(': #down
            outs=sofar+str(eval_until_close(strit)) #new sofar empty, push new call on stack
            print(f'opencase:{outs}')
            return outs # we know close paren occurred, then eval, then eval_until_close() have each returned
        elif n==')' :  # up
            outs=str(eval(sofar)) #existing sofar eval'd... returns python types,here we need str for next eval()
            print(f'closecase:{outs}')
            return outs
        else: #across
            print(f'sofar+n:{sofar+n}')
            eval_until_close(strit,sofar+n) #existing sofar+=n, move along by a char
    except StopIteration: return sofar #print('ran off end before last closing )')

def walk_tree_T(strit,sofar='',closetoken=None,somedumbfun=lambda x:x):
    '''ExmpB Chew and walk gum at the same time! Template....
    strit is iterator of open/close tokens and obj sequences
    Validate and modify iterator of objects with grammars like:
        obj -> opentok obj closetok'''
    tokens={'{':'}','(':')','[':']'} #dict of open:close token key:val pairs
    try:
        n=next(strit)
        if n in tokens: # down a level
            return sofar+walk_tree_T(strit,closetoken=tokens[n],somedumbfun) # sofar containerish/elem obj must impl def  __add__(self=containerish,elem), also overide default sofar=''
        elif n=closetoken: # up a level
            return somedumbfun(sofar) #obj/calculation/split(str)/populate a tree/etc...
        else: #across one element by exclusion of not up nor down
            walk_tree_T(strit,sofar+n,closetoken,somedumbfun) # sofar.__add__(elem()n) must be defined for type of n/sofar
    except StopIteration: return sofar # the very top-level null/missing/moot closetoken if no corr opentoken like \0 byte

def walk_tree_objarr(strit,sofar,tokens={'{':'}','(':')','[':']'},closetoken=None,somedumbfun=lambda x:x):
    '''ExmpC de-serialize iterator, strit of obj(s) or grouping-delimiting token chars
    Validate and modify iterator of objects with grammars like:
        O -> O | opentokOclosetok eg. (O) | {O}
        O -> objecttok,O | objecttok #left recursion, literal comma
        No lexer as single char open/close/comma- tokens
        '''
    if not sofar: sofar=[] # setting a default in signature will be a single shared instance
    try:
        n=next(strit)
        if n in tokens: # down a level
            return sofar.append(walk_tree_objarr(strit,closetoken=tokens[n],somedumbfun)) # sofar containerish/elem obj
        elif n=closetoken: # up a level
            return somedumbfun(sofar) #obj_list- or obj_single- calculation/split(str)/populate a tree/etc...
        else: #across one element by exclusion of not up nor down, not going to work if extend input format later...XML raisondetre
            walk_tree_objarr(strit,sofar.append(n),closetoken,somedumbfun) 
    except StopIteration: return sofar # the very top-level null/missing/moot closetoken if no corr opentoken like \0 byte

