class RecRet:
    def recur(s,inp):
        inp=inp[1:]
        print(inp)
        if(inp != ''):
            return var=s.recur(inp)
        else: 
            return True # done
    def calling_fun(s):
        s.recur('asdfa')
        return 
r=RecRet()
print(r.recur('four'))
print('cf: '+str(r.calling_fun()))
