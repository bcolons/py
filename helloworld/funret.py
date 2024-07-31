def myfun(f):
     return f
def thyfun(f):
     return f()

print(myfun(lambda: 2+2+3)) # returns a function
print(myfun(lambda x: x+ 2+2+3)) # returns a function
print((myfun(lambda x: x+ 2+2+3)(4))) # an actual value - 11

print(thyfun(lambda: 2+2)) # actual evaluated value - 4
