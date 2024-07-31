import weakref
import collections # namedtuple...static binding of field names/values ...not useful here

class Interndict:
    '''Arbitrary intern'd dict entries. 
    Supports is/id() op and saves space (and make all of them garbage-uncollectable '''
    _dict_arr=[]
    #_dict_arr=set() # fails as dict/list/set unhashable, apparently bc_1

    @classmethod
    def __id__(cls,self): # never called, id(..) -> type(obj).id(obj)
        return 1
#    def __hash__(s):
#       hashval=0
#        for each in self.keys():
#            hashval = hashval ^ hash(each)
#        return hashval
    def __new__(self,**objargs): # actually returns a dict() not an Interndict()
        for each in self._dict_arr: 
            if each == objargs: # already exists case
                return each
        #self._dict_arr.append(tuple(objargs)) # tuple breaks is-test ...
        self._dict_arr.append(objargs) # new dict case
        #self._dict_arr.add(tuple(iter(objargs.items()))) # new dict case , set impl fails per bc_1
        return objargs

aa=Interndict(temp='mild',sky='cloudy')
ab=Interndict(course='marathon',dist='26.2')
ac=Interndict(course='marathon',dist='26.2')
ad=Interndict(dist='26.2',course={'ny','marathon'})
#print(aa.__hash__())
#print(ab.__hash__())
print(id(aa))
print(id(ab))
print(id(ac))
print(aa==ab)
print(ab==ac)
print(aa is ab)
print(ab is ac)
print(type(aa))

