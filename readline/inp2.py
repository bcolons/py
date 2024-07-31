import readline # adds up-arrow-history in case of python -S
import rlcompleter # add tab-complete methods
#readline.parse_and_bind('tab: complete') --not needed, only need: import readline
def interploop():
    hist=[]
    while True:  # input-eval_rhs-exec loop, simple python interactive interpreter with two kinds of inputs, expressions and assignments
        # either '=' or '==' may be present, if both is treated as an expression
        chars=input()
        #hist.append(chars.strip())
        if('=' in chars and '==' not in chars): 
            #hist.append(str(chars).strip())
            print('hist: ')
            print(hist)
            lhs=[]
            rhs=[]
            done=False
            for each in chars:
                if(not done):
                    done = each == '='
                if(not done ): # prior to '='
                    lhs.append(each)
                elif(done and each != '='):   # after '=' 
                    rhs.append(each)
#                else: 
#                    continue #skip '='
            print(f'{str(lhs)} = {str(eval(str(rhs)))}') # eval 
            exec(chars)
        else : print(eval(chars)) # expressions incl. both = and == case
interploop()
