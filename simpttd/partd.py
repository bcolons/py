import doctest
class PartD:
    '''Class wraps a dict but adds a pending_key field (a 'Part-ial D-ict pair') which is used for a subsequent dict.update([(pending_key,'value')]).
    Used by ReqResArch (file persistent req/res archive), bc_server.py (incoming request), and bc_shutils.py (outgoing response). 
    Not threadsafe, instead use implementation with doubd.py and code a request.persistentid() for keys
    >>> d=PartD()
    >>> d.next_key('key1')
    >>> d.update1('val1')
    >>> d.__dict__
    {'dd': {'key1': 'val1'}, 'nextkey': 'key1', 'keyset': False}
    '''
    def __init__(self):
        self.dd={}
        self.nextkey=''
        self.keyset=False
    def next_key(self,nextkey): # set up first part of a key/val pair, nthdsafe 
        '''After the request is parsed call next_key(request_string), once response is ready call  update1(response_string)'''
        self.nextkey=nextkey
        self.keyset=True
    def _update(self,arr):  # private commit key/val pair to archive, same as dict.update(..), doesnt check if existing key is valid or dirty, nthdsafe
        '''Private wrapper for dict.update(..). Only called by update1(..)'''
        self.dd.update(arr)
    def update1(self,value,key=''):
        '''Public method to update the archive with req/res pair once the response field is ready.'''
        if self.keyset:
            self._update([(self.nextkey,value)]) #not thdsafe
        self.keyset=False
    def myrepr(self):
        '''Generic override for builtin _repr__ which adds (barely) formatted member data'''
        return f'{self.__class__} at {hex(id(self))}: {self.__dict__}'
    def sl_repr(self): # make a string list of useful formatted member data 
        '''Generic pattern to (concisely) display state of a selection---unlike the all-in: print(myobj.__dict__) ---of data members using a list comp.
        Usage: print(*myobj.sl_repr())'''
        return  ['self.nextkey: '+self.nextkey +'; ' +self.dd.__str__() if self.keyset==True else self.dd.__str__()]

if(__name__=='__main__'):
    d=PartD()
    print(*d.sl_repr())
    d.next_key('key1') 
    print(*d.sl_repr())
    d.update1('val1')
    print(*d.sl_repr())
