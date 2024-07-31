class Intern:
    '''Trivial mixin factory to make generic instances singletons allowing identity/'is' tests...
    No mutating methods should be available in the mixed-in class
    Objects passed to __new__ should overide; 
    A hash(..) to enable == op
    B id(..) to enable 'is' op
    with suitable choices from __str__/__repr__/etc/...'''
    _dict = dict()

    @classmethod
    def _construct(cls, obj):
        try:
            return cls._dict[obj]
        except KeyError:
            cls._dict[obj]=obj 
            return obj
    @classmethod
    def try_id(cls,obj):
        try:
            return id(cls._dict[obj])
        except KeyError:
            return None
        
    def __new__(self,obj):
        return __class__._construct(obj)

class Tuptern(Intern):
    '''Anything hashable...'''
    def __init__(self,tup):
        return super()._construct(tup)
#        return __new__(tup)
    def __id__(self):
        return  super().try_id()
        #for each in 
        #return id(self.d)
        #return None
    def __hash__(self):
        return 1

#k=Intern._construct('hey');l=Intern._construct('hey')
#k=Intern(object()); l=Intern(object())
k=Tuptern((1,2,3)); l=Tuptern((1,2,3))
h=Tuptern(('a','quick','fox'))
i=Tuptern(('a','quick','fox'))

print( k is l)
print( h is i)
print( id(k) ,id(l))
