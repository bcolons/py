class TreeNode():
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data

    def trav(self,tnode):
        res = []
        if(tnode):
            res=self.trav(tnode.left)
            res.append(tnode.data) 
            print(tnode.data)
            res = res + self.trav(tnode.right)
        return res

    def insert(self,data):
        if(self.data):  
            print(self.data)
            if data < self.data:
                if self.left is None:
                    self.left=TreeNode(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right=TreeNode(data)
                else:
                    self.right.insert(data)

if(__name__=='__main__'):
    r=TreeNode(27)
    r.insert(23)
    r.insert(13)
    r.insert(33)
    r.insert(28)
    r.insert(29)
    print(r.trav(r))
    
        
