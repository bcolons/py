def lams(ct=None):
    def inner(cti=0):
        i=0
        agg=0
        while i < cti:
            agg+=i
            i+=1
        return agg
    if not ct: return inner
    else: return inner(ct)

def lams2(ct=None):
    i=0
    agg=0
    if ct: 
        while i < ct:
            agg+=i
            i+=1
            return agg
    else: return lams2

inst=lams()
print(lams())
print(lams(ct=9))
print(inst(cti=5))
            
inst=lams2
print(inst)
print(inst())
print(inst(ct=5))
