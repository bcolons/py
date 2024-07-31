import collections.abc as abc
'''asdf'''
class  myIterator(abc.Iterator):
    def __iter__(self):
        return super.__iter__(self)
    def __next__(self):
        return next(super)
i=myIterator()
next(i)
    
    
