class Itree:
    """
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
    """
    def neckst( self, ist):
        node=None
        skip_flat_iter=False
        print("23, preiterd: "+str(ist))
        try:
            node=next(ist)
        except StopIteration:
            skip_flat_iter=True
            print("33, StopIterd exception: node=next(ist) failed: "+str(ist))
            return
        first_child_node=None
        try:
            first_child_node=next(node)
            print("37, ChildIter exists: "+str(first_child_node))
            neckst(first_child_node)
        except TypeError:
            skip_flat_iter=True
            print("42, ChildIter raised exception: first_child_node=next(node) "+str(first_child_node))
        if(not skip_flat_iter):
            print(str(node))
            neckst(ist)
if(__name__=='__main__'):
    myl=["a","b","cc","dew"]
    myk=["egg","flat",["germ",myl,["deeper",myl,"trieste"]]]
    print(f"source tree is {myk}")
    lt=Itree()
    lt.neckst(myk)

# example
# ist= [a,b,[c,e],[f,g]]
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
