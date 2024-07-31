import weakref
import builtins

class Imdict(dict):
    '''Immutable dict (may be used as a hash key/elem of set/dict)'''
    def __hash__(self):
        return hash(tuple(self.items()))
    def pop(self):
        raise NotImplemented
    def __setitem__(self, key, value):
        raise NotImplementedError

class Interndict:
    '''Arbitrary intern'd dict, supports is/id() op and saves space (and make all of them garbage-uncollectable 
    Essentially we create a way to hash dict's/use dict's as keys because we can't natively (mutables are unhashable)'''
    class _dict(dict):
        '''Immutable dict (may be used as a hash key/elem of set/dict)'''
        def __hash__(self):
            return hash(tuple(self.items()))
        def pop(self):
            raise NotImplemented
        def __setitem__(self, key, value):
            raise NotImplementedError
    _dict_arr=dict()  # dict of myhashval:dict entries

    def __new__(self,**objargs):
        '''Before generating an obj ref, 
        A lookup a hash(input dict) 
        B if already exists 
             C return it 
        D else add a new one'''
        out_obj= self._dict(objargs)
        out_hash= out_obj.__hash__() 
        try: 
            print('tryin... ',out_hash,out_obj)
            return self._dict_arr[out_hash] # already exists case
        except KeyError:
            print('except... ',out_hash,out_obj)
            self._dict_arr[out_hash]=out_obj # new dict case 
            return out_obj
        
def myhash(d): # need some way to transform unhashable dict, before archiving it as dict[hashable key]= orig dict val
    return tuple(d.items())

aa=Interndict(temp='mild',sky='cloudy')
ab=Interndict(course='marathon',dist='26.2')
ac=Interndict(dist='26.2', course='marathon')
ad=Interndict(dist='26.2',course=['ny','marathon'])
ae=Interndict(dist={'mi':{'the','unit','we','use','26.2'}},course=['ny','marathon'])

#print(aa.__hash__())
#print(ab.__hash__())
print(id(aa),myhash(aa))
print(id(ab),myhash(ab))
print(id(ac),myhash(ac))
print(id(ae),myhash(ae))
print('a eq b:f ',aa==ab,aa.__eq__(ab)) 
print('b eq c:t ',ab==ac)
print('e eq a:f ',ae == aa)
print(aa is ab)
print(ab is ac)
print(ae is aa)
print((Interndict._dict_arr))

