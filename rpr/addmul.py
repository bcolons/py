'recursively add and mult digits in input string'
a='6+4*2+3*4+5+4' #not th ebest exmp...ooo...better / more-general would have explicit grouping
b='6+(4*2)+(3*4)+5+4'
c='((6+(4*2))+(3*4))+5+4'
d='(((6+(4+2))+(3+4))+5)+4' #easiest explicit groups single operator with two operands...should have simplest evaluator, each (..) is an iterator
e='4+6*8+2*5'
f='((((4+6)*8)+2)*5)' #single pass, lhs accumulates
''' 6+go(rest)
6+4*go(rest)...
A. need to build tree and traverse tree.two steps in general 
 or
B. eval-apply loop
C. both A,B are exactly the same....
 
three patterns: lit op exp, lit op lit, exp op lit (really?)
'''
def eval_until_close(strit,sofar=''):
    '''Return result of parenthically nested evaluatable stuff'''
    try:
        n=next(strit)
        if n=='(': sofar+eval(eval_until_close(strit)) #new sofar empty
        elif n==')' : return eval(sofar) #exisiting sofar eval'd
        else: eval_until_close(strit,sofar+n) #existing sofar+=n, move along by a char
    except StopIteration: print('ran off end before last closing )'
def maketree(stit):
    '''Return a tree of [lhs op rhs] nested lists from a (flat) string iterator with digits and arithemetic operators'''
    out=[]
    try:
        n=next(stit)
        if n=='

def simp_muls(): pass
'Run and return mult val if both operands ow push ("return") a call to mult(val,expr)'
def dispatch(stit): #do we need assignment/accumulator? hopefully not...use the stack!....later....
    '''Apply add operations in correct parenthetical order, ie. operations involve only two operands always, lhs rhs
    A. Manage parens
    B. Assemble and eval lhs op rhs expressions
    grammar is:
        expr -> digit op digit | expr op digit | expr op expr | digit op expr
        '''
    accum=0
    try:
        n=next(stit)
        if n=='(': #expr coming
            accum+=get_l(stit) #descend one level in 'tree'
        elif n==')':  #ascend one level up 'tree'...dont really need this paren if only lhs op rhs format...
        else: return get_o(stit,n) # no initial open paren

def get_l(stit):
    try:
        get_o(stit,next(stit))
    except StopIteration: print('missing last lhs...')
def get_o(stit,lhs):
    try:
        get_r(stit,lhs,next(stit))
    except StopIteration: print('missing last op...')
def get_r(stit,lhs,op):
    try:
        return eval(lhs+op+next(stit)) # what happens now? this value is by def a new lhs...or the final lhs
    except StopIteration: print('missing last rhs..')

'''get_r(rest): get_o((rest,lhs_val)
get_o(rest,lhs):  get_r(rest,lhs,op) #also parse_open(rest), parse_close(rest)
def dispatch(stit):
if ch==lhs set lhs=ch;parse_op + next()
if ch==op do 
if ch==rhs eval (lhs op rhs)
def maketre(chpat,stit=None):pass
def push_next_op_next_operand():
    'append an operand to prior op and append next op'
'''
+ 6 go(rest)) 6+ consumed
+ 6 * 4 go(rest) 4* consumed
plus(6,mult(4,2)).plus(go(rest))) 2+ consumed
plus(6,mult(4,2)).plus(3,mult(go(rest))) 3* cd
'''
def evaltre(tre): pass

6+4; lhs =6, stit=+4; lhs=6,op=+,stit=6; lhs=6,op=+,rhs=4;eval(lhs+rhs)
(6+(4+1));ch=(,stit=..;




