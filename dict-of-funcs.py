class asdf:
    def func(a,b):
        return a-b
    def funcp(a,b,c):
        return a+b+c

    def __init__(self):
        self.arr = [self.func, asdf.funcp]
        self.fdict = {'one':asdf.func, 'two':asdf.funcp}
a=asdf()
#print(str(a.arr[0](4,3)))
#print(str(a.arr[1](3,5,5)))
print(str(a.fdict['one'](3,5)))
print(str(a.fdict['two'](3,5,5)))
