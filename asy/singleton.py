class C:
    def __init__(self,singleton=[]): # compile-time empty list is allocated, shared across instances
        self.root=singleton
        try:
            self.root[0]+=1
        except IndexError:
            self.root.append(1)
    
    def count(self):
        print(self.root[0])

    def inc(self):
        self.root[0]+=1
def main():
    a=C()
    a.count()
    b=C()
    a.count()
    while True:
        import pdb;pdb.set_trace()
        print(a.root[0]) 
        
            
