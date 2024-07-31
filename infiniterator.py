import collections.abc as abc
class Infiniterator(abc.Iterator): #only needs concrete __next__()
    '''Infinite iterator
    Implements __next__() (which runs forever) and inherits from Iterator'''
    def __next__(self):
        return True

infator=Infiniterator()
for i in infator:
    break # o/w will print infinite num of True print(i)
    print(i)

#class Infiniterable(abc.Iterable): # only needs concrete __iter__()
class Infiniterable():  # has-a iterator, no need to inherit from Iterable
    def __init__(self):
        self.internal=Infiniterator()
    def __iter__(self):
        return self.internal

infable=Infiniterable()
for i in infable:
    break # o/w will print infinite num of True print(i)
    print(i)

class InfIterSub(Infiniterator):
    def __iter__(self):
        return super.__init__(self)
iis=InfIterSub()
for i in iis:
    print('elk')

