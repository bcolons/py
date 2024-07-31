class a:
    class singlet:
        def __hash__(self):
            return 3
        def __id__(self): # never called
            return 4
    _dict=singlet()

    def __id__(cls,self):
        return 1 # never returned
    def __hash__(s):
        return 2 # never returned,  instead type(obj).__hash__(obj), above or builtin o/w
    def __new__(self):
        return self._dict
        #if self._dict != None:
            #return self._dict
        #else:
            #self._dict=self.singlet()
    

aa=a()
ab=a()
print(hash(aa))
print(hash(ab))
print(id(aa))
print(id(ab))
print(aa==ab)
print(aa is ab)
print(type(aa))

