class Imdict(dict):
    '''Immutable dict (may be used as a hash key/elem of set/dict)'''
    def __hash__(self):
        return hash(tuple(self.items()))
    def pop(self):
        raise NotImplemented
    def __setitem__(self, key, value):
        raise NotImplementedError

print(d:={1:11,2:22})
print(dd:={1:11,2:22})
print(e:=Imdict(d))
print(e.__hash__())
print(f:={e})
print(f.__contains__(e))
# e[3]=33

    
