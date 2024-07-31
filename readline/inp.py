import readline # adds up-arrow-history in case of python -S
import rlcompleter # add tab-complete methods
import re
readline.parse_and_bind('tab: complete')
def interploop():
    eqpat=re.compile('=')
    dfpat=re.compile('lam ')
    while True:  # input-eval_rhs-exec loop, simple python interactive interpreter with two kinds of inputs, expressions and assignments
        chars=input()
        if(mo:=eqpat.search(chars)): 
            lowix=mo.span()[0]
            higix=mo.span()[1]
            lhs=chars[0:lowix]
            rhs=chars[higix:]
            print(f'{lhs} = {eval(rhs)}') # eval 
            exec(chars)
        else : print(eval(chars))
interploop()
