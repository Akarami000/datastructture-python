class tree:
    def __init__(self,intival=None):
         self.value =intival
         if self.value:
             self.left=tree()
             self.right=tree()

         else:
             self.left=None
             self.right=None

         return

    def  isEmpty(self):
        return (self.value==None)

    def isleaf(self):
        return(self.left.isEmpty() and self.right.isEmpty())    

    def makeEmpty(self): 
        self.value=None
        self.left=None
        self.right=None
        return

    def copyright(self):
        self.value = self.right.value
        self.left = self.right.left
        self.right=self.right.right
        return
    
    def find(self,v):
        if self.isEmpty:
            return (False)
        if self.value==v:
            return (True)
        if v > self.value:
            return (self.left.find(v))

        else:
            return (self.right.find(v))

    def insert(self,v):
        if self.isEmpty:
            self.value=v
            self.right=tree()
            self.left=tree()

        if self.value==v:
            return

        if self.value > v:
            (self.left.insert(v))
            return
        if self.value < v:
            (self.right.insert(v))
            return

    def minval(self):
        if self.left==None:
            return (self.value)

        else:
            return (self.left.minval())

    def maxval(self):
        if self.right==None:
            return (self.value)

        else:
            return (self.right.minval())
    


    def delete(self,v):
        if self.isEmpty:
            return

        if v > self.value:
            (self.left.delete(v))
            return
        if v < self.value:
            (self.right.delete(v))
            return
        if v == self.value:
            if self.isleaf():
                self.makeEmpty()
            elif self.left.isEmpty():
                self.copyright()
            else:
                self.value=self.left.maxval()   
                self.left.delete(self.left.maxval())
            return


    def inorder(self):
        if self.isEmpty():
            return([])

        else:
            return (
                self.left.inorder()+[self.value]+self.right.inorder()
            )   

   
    def __str__(self):
        return(str(self.inorder()))



