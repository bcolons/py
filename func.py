# no arg func's
def nafunc():
    return 99
def ninenine():#ret a fun that calls nafunc ---must eval result with '()'  to get fun val
    return lambda: nafunc() 
def ninenine_no_parens():# ret a fun (lambda) that returns a fun that calls nafunc--- must eval result with two '()' 
    return lambda: nafunc  # dont need lambda, see following....once you name a func, use it by name!
def nine9_no_parens(): # equiv to ninenine()
    return nafunc #func ptr ? func ref? again, equiv to 'return lambda: nafunc()'
def printcom(arg):
    print('# '+str(arg))
printcom(ninenine()()) # 99
printcom(ninenine_no_parens()()()) # 99 but need extra parens
printcom(nine9_no_parens()())  #99 , equiv to imd preceeding

#single arg func's
def funfunc(func, arg):
    return func(arg)
def add1(arg):
    return arg+1
def ladd1(arg): # dont need lambda, see next def
    return (lambda x: add1(x))(arg)
def nladd1(arg):
    return (add1)(arg)

def plain_add1(arg):
    return add1(arg)
def just_func():
    return add1
def just_func_ign_1arg(arg):
    return add1

def ladd1na(): # allowed but doesnt make sense, signature/prototype mismatch will always raise TypeError at rt never compile time
    return lambda x: add1(x)

# below pair equiv
printcom(funfunc(add1, 2)) # 3
printcom(ladd1(2)) # 3
printcom(nladd1(2)) # 3
printcom(plain_add1(2)) # 3
printcom(((just_func)()(2))) #  3
printcom((just_func_ign_1arg)(2)(9)) # 10 , 2 inp ignored just like just_func1arg ignores its arg
#fail printcom((ladd1na)(2))
