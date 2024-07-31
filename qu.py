'''Various ways to implement stream parsing: recursive-return, recursive-yield, iterative-return, iterative-yield (most concise and 'tail-recursive-ish') '''
def uq(strit,sq=None):
    '''Take a paren-nested LISP-style string and python3.12 single/double quote nest it'''
    n=None
    try:
        n=next(strit)
    except StopIteration: return ''
        #print(n,sq)    
    if(n=='(' and sq==None):  return n+uq(strit,True) #initial paren is defined a single quote
    
    elif((n==')' or n=='(' ) and sq==True): return "'"+uq(strit,sq=False)
    elif((n==')' or n=='(' ) and sq==False): return '"'+uq(strit,sq=True)
    else: return n+uq(strit,sq)
def qu(strit,sq=None):
    '''Take a python3.12 single/double quote string and paren-nest it, LISP-style '''
    n=None
    try:
        n=next(strit)
    except StopIteration: return  ''
        #print(n,sq)    
    if(n=='"' and (sq==True or sq==None): return "("+qu(strit,False)  #first open single q/double q cases; reallty need counters or stack
    elif(n=="'" and (sq==False or sq==None): return "("+qu(strit,True)
    elif(n=='"' and sq==False): return ")"+qu(strit,sq=True)
    elif(n=="'" and sq==True): return ")"+qu(strit,sq=False)
    else: return n+qu(strit,sq)

def uqi(strit):
    '''Take a paren-nested LISP-style string and python3.12 single/double quote nest it'''
    sofar=''
    sq=None
    try:
        n=next(strit)
        if(n=='(' and sq==None):  
            sofar+"'"
            sq=True
        else: sofar+n
        while True:
            n=next(strit)
            if(n=='(' and sq==True):  
                sofar+'"'
                sq=False
            elif(n=='(' and sq==False):  
                sofar+"'"
                sq=True
            elif(n==')' and sq==True):  
                sofar+"'"
                sq=False
            elif(n==')' and sq==False):  
                sofar+'"'
                sq=True
            else: sofar+n
    except StopIteration: return sofar
def qui(strit):
    '''Take a py312 single/doub quout nest return paren-nested LISP-style string '''
    sofar=''
    sq=None
    try:
        while True:
            n=next(strit)
            if(n=="'" and sq==True):  
                sofar+')'
                sq=False
            elif(n=="'" and (sq==False or sq==None)):  
                sofar+"("
                sq=True
            elif(n=='"' and sq==True):  
                sofar+"("
                sq=False
            elif(n=='"' and (sq==False or sq==None)):  
                sofar+')'
                sq=True
            else: sofar+n
    except StopIteration: return sofar
def uqy(strit):
    '''Take a paren-nested LISP-style string and generate python3.12 sing/doub quote nested version '''
    sq=None # could set to False to force first paren is always sing q, also we arent validating for all-matched
        while True:
            n=next(strit)
            if(n=='(' and sq==True):  
                yield '"'
                sq=False
            elif(n=='(' and (sq==False or sq==None)):  #None is first paren case, defined to output sing q
                yield "'"
                sq=True
            elif(n==')' and sq==True):  
                yield "'"
                sq=False
            elif(n==')' and sq==False):  
                yield '"'
                sq=True
            else: yield n
def quy(strit):
    '''Take a py312 sing/doub quot nest generate paren-nested LISP-style string 
    Input grammar is:
        S -> sq S sq | dq S dq | char S | char
    Output grammar is:
        S -> ( S ) | char S | char
    '''
    sq=None # None is no open quotes or top level, True is open single q, False is open doub q
    # (...not that it makes any difference as its all parens out...its just proper CFL parsing)
    sqn=0 # open sing q counter, neg is bad inp, both should be 0 at end of inp
    dqn=0 # open doub q counter
    def is_top(sq, sqn,dqn): # helper to update sq whenever top level / no open q case 
        if(sqn == 0 and dqn == 0): return None
        else: return sq
    while True:
        n=next(strit)
        if(n=="'" and sq==True):  
            yield ')'
            sqn-=1
            sq=False
            sq=is_top(sq,sqn,dqn)
        elif(n=="'" and (sq==False  or sq==None)):  #None is initial first q as sing , also top level no-open quotes
            yield "("
            sq=True
            sqn+=1
            sq=is_top(sq,sqn,dqn)
        elif(n=='"' and (sq==True  or sq==None)):  #None is an initial first q as doub 
            yield "("
            sq=False
            dqn+=1
            sq=is_top(sq,sqn,dqn)
        elif(n=='"' and sq==False):  
            yield ')'
            sq=True
            dqn-=1
            sq=is_top(sq,sqn,dqn)
        else: yield n
