class Ltree:
    def __init__(self):
        self.iden=0
        self.ct=0
    def print_node(self, n):
        print('|_'+'__ '*self.iden+str(n),end='\n')
    def print_list(self, n):
        print('|_'+'__ '*self.iden+str(n),end='\n')
    def trace(self,ist,ix):
        print(f"\nround:{self.ct}\ncur list:",end='')
        self.print_list(ist)
        print("cur node:",end='')
        try:
            self.print_node(ist[ix])
        except IndexError:
            pass
        print("\n")

    def isLast(self, lst, ix):
       try:
            tmp=lst[ix+1]
            return False
       except IndexError:
            return True
         
    def neckst( self, lst, ix):
        self.trace(lst,ix)
        self.ct+=1
        if(self.isLast(lst,ix)):
            self.iden=self.iden-1
            try:
                self.print_node(lst[ix])
            except IndexError:
                pass
            finally:
                return
        elif(self.isList(lst,ix)):
            self.print_list(lst)
            self.iden=self.iden+1
            self.neckst(lst[ix],0)
        self.print_node(lst[ix])
        self.neckst(lst,ix+1)

    def isList(self, lst, ix):
        try:
            s= (str(type(lst[ix])) == "<class 'list'>")
            if(s):
                return True
            else:
                return False
        except IndexError:
            return False
if(__name__=='__main__'):
    myl=["a","b","cc","dew"]
    myk=["egg","flat",["germ",myl,["deeper",myl,"trieste"]]]
    print(f"source tree is {myk}")
    lt=Ltree()
    lt.neckst(myk,0)

# example
# lst= [a,b,[c,e],[f,g]]
#two tests: isLast and isList

#traverse(mylist,index)
#    for elem in mylist
#        if isList traverse(mylist[index][0]
#        print elem
#        elif isLast traverse(parent-of-mylist
#        else traverse(mylist,index+1)
#
#pr(ist,0,N,N)
# print ist[0] 
# pr(ist,1,N,N)
#  print ist[1]
#  pr(ist,2,N,N)
#   pr(ist,2,[c,e],0)
#    print [c,e][0]
#    pr(ist,2,[c,e],1
#     print [c,e]1
#     isLast ==True
#     return
#    return
#  pr
