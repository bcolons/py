import inspect as i
import copy
def deepc(obj,sofar=None):
    '''Return a deep copy, 'sofar', of 'obj' and recursively any contained objects via obj.__dict__ 
    1. Traverse obj.__dict__ for 'copiables'
    2. Make a shallow copy of each key and each value  
    3. Add each to the emerging deep copy (tree) object with the same i.object-type, ii. data and iii. correct heirarchy 
    Fixme: Currently we copy intermediate obj's but the leaf object dicts use original refs for values'''
    if not sofar:
        sofar=copy.copy(obj) # the root of the deepcopy.__dict__ tree of shallow copied objects, want it to both look and be uniq from ex below
    try:
        for each in sofar.__dict__:
            sofar.__dict__.update(copy.copy(obj.__dict__)) # add a shallow copy of key and value to sofar tree, next recur step writes a deep copy of val
            deepc(sofar.__dict__[each],sofar.__dict__) # replace shallow copy values with deep copy
    except AttributeError: # only to catch primitives that dont have a __dict__ member; to use a primitive wrap each in java-style Object()'s
        pass # sofar.__dict__ not iterable
    except TypeError:
        pass # sofar.__dict__ not iterable, ie. is a primitive lacking __dict__ member
    return sofar
    
def bc_dcopy(obj): 
    newob=copy.copy(obj)   
    newob.__dict__=copy.copy(obj.__dict__)
    for each in newob.__dict__:
        try:
            newob.__dict[each]=bc_dcopy(copy.copy(obj.__dict__[each]))
        except AttributeError:
            print (f'AttributeError with a primitive:  obj.__dict__[{each}] or newob.__dict__[{each}]') #usually primitive lacking a __dict__
    return newob
def bc_copy(obj): # is this the same as copy.copy() ? Yes...
    newob=copy.copy(obj)   
    newob.__dict__=copy.copy(obj.__dict__)
    return newob
class NullC:
    pass
class FlatA:
    def __init__(self,char):
        self.data=char
class FlatB:
    def __init__(self,char):
        self.data=char
class FlatC:
    def __init__(self,char):
        self.data=char
if(__name__=='__main__'): # runtime has-a relationship's
    a=FlatA(NullC())
    b=FlatB(a)
    c=FlatC(a)
    d=FlatA(b)
