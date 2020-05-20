################ to create nodes ##################
class node:
    def __init__(self,intval=None):
          self.value=intval
          self.next=None

    def isEmpty(self):
        return( self.value== None)      




##############################3

    def append(self,v):
        if self.isEmpty():
            self.value=v

        elif self.next== None:
            newnode = node(v)
            self.next = newnode

        else:
            self.next.append(v)

        return()


    def insert(self,v):
        if self.isEmpty():
            self.value= v
            return()

        newnode = node(v)

        (self.value, newnode.value)=(newnode.value,self.value)
        (self.next,newnode.next)=(newnode.next,self.next)

        return()


    def deleter(self,v):
        if self.isEmpty():
            return ()

        if self.value==v:
            if self.next == None:
                self.value=None
            else:
                self.value=self.next.value
                self.next=self.next.next
                return() 

        else:#recurcive delete
            if self.next!=None:
                self.next.deleter(v)
                if self.next.value== None:
                    self.next=self.next.next
            return()


    def __str__(self):        
        selflsit=[]
        if self.value==None:
            return(str(selflsit))
        temp =self
        selflsit.append(temp.value)
        while temp.next != None:
            temp=temp.next
            selflsit.append(temp.value)
        return(str(selflsit))    







        