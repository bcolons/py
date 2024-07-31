import sys
class ListCompEx:
    def __init__(s):
        s.inp=''
lce=ListCompEx()
lce.inp= open(sys.argv[1],'r')
list_comp = [line.strip() for line in lce.inp if line != ''] # list comprehension
for l in list_comp:
    print(l)
lce.inp= open(sys.argv[1],'r')
generator_exp = (line.strip() for line in lce.inp if line != '') # equiv generator exp 
for n in generator_exp:
    print(n)
for m in (e+1 for e in range(19) if e%3): # generator expression , 0 is False
    print(m)
