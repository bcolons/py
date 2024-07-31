def fun1():
    return 'fun1'
print(fun1()) #fun1

def fun1(a, b='b'):
    return b

def fun1(a,b,c):
    return a

print(fun1()) # 'b'
print(fun1('r')) # 'r'
print(fun1()) #'b'
print(fun1(b='bbb')) # 'bbb'
#print(fun1(a='aaa')) #T ypeError unexpect keyword 'a'

#summary: latest declaration is used (ie. think interactive interpreter behavior).
# Different function prototypes and definitions are not allowed. 
