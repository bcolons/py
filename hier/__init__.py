import time
class Hh:
    '''Simple Base and Subclass example showing __new__/__init__ sequence.'''
    last_hstamp=time.time()
    def __new__(cls):
        print(f'{id(self)}{self} Hh.new: ')
        Hh.nowd()
        #self.summem='sumin' not working...or adds class mem instead
        return 
    def __init__(self):
        Hh.nowd()
        self.summem='sumin'
        print(f'{id(self)}{self} Hh.inniyit: ')
    def supmeth(self):
        return 'supmeth'
    @staticmethod
    def nowd():
        now=time.time()
        delta=now-Hh.last_hstamp
        Hh.last_hstamp=now
        print(delta)
class Ii(Hh):
    def __new__(self):   # self is really cls
        print(f'{id(self)} Ii.new: ')
        super().__new__(self)
        Hh.nowd()
    def __init__(self):
        print(f'{id(self)} Ii.init: ')
        Hh.nowd()
print('tt',time.time())
Hh.nowd()
