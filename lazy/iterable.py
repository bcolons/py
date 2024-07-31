import time
class c():
    def __init__(self,max):
        self.max=max
        self.ct=0
        self.data=(1,2,3)
#    def __iter__(self):
#        while self.ct != self.max:
#            self.ct+=1
#            yield self
    def r_iter__(self):
        for each in self.data:
            yield each #doesnt raise StopIteration on return in builtin usages/contexts (for...in itrbl: ...others?)`

    def __getitem__(self,ct): 
        ''' Used in; for....in something_infinite_or_finite: 
        which terminates iff StopIteration is raised'''
        return 'hey'# self.data[ct]
        
    def r_next__(self):
        self.ct+=1
        return self.data[self.ct-1]
        #raise StopIteration # return None isn't the right thing here

    def __str__(self):
        return str(self.ct)

ci=c(10)
for each in ci:
    print(each)
def simp_gen_fun():
    while True:
        yield time.time

g=simp_gen_fun()
a=[]
#for yielded in 
for each in range(3):
    a.append(next(g))
for yielded in iter(a):
    print(yielded() )
    time.sleep(1)
