a='a','b'
c=a,'a','b'
d=c,'a',c,'b'
#TypeError: print(" "+a) TypeError 'can only concat str not tuple'
#TypeError: print(type(next(c))) 'tuple obj is not an iterator'
print(type(c)) # "<class 'tuple'>"
#TypeError: print(type(next(c))) 'tuple obj is not an iterator'
print(next(iter(d))) # (a,b),c...etc

e=['f','g']
h=[e,'i',e]
#TypeError: print( ' '+e) "can only concat str (not list) to str
#TypeErro: print(next(e)) list obj is not an iterator
print(next(iter(e))) # 'f'
print(next(iter(h))) # [f,g]

j={"k","l","m"}
#TypeError: n={j,"o","p"} " unhashable type: set"
#TypeError: print(" "+j)  "can only concat str (not set) to str"

q ={"r":"rabbit", "s":"shadow"}
#TypeError: print (" "+q) "can only concat type str (not dict) to str"
#SyntaxError: t = {q, "u":"unterwasser"} "invalid syntax"
