class node:
    def __init__(self,data=None):
        self.data= data
        self.next= None

class LinkList:
    def __init__(self):
        self.head= node()

    def append(self,data):
        newN=node(data)
        cur= self.head      
        while cur.next != None:
            cur=cur.next
        cur.next=newN    

    def length(self):
        cur= self.head
        total=0
        while cur.next != None:
            cur= cur.next
            total += 1
        return(total)
    def display(self):
        cur= self.head
        elem=[]
        while cur.next != None:
            cur= cur.next
            elem.append(cur.data)
        print(elem)    


    def get(self,index):
        if index>=self.length():
            print('ERROR: "erase" Index out of range')
            return None
        cur_idx=0
        cur_node=self.head
        while True:
            cur_node=cur_node.next
            if cur_idx == index: return  cur_node.data
            cur_idx +=1    

    def erase(self,index):
        if index>=self.length():
            print("error:'Erase'Index out of range ")
            return  None
        cur_idx=0
        cur_node=self.head
        while True:
            last_node = cur_node
            cur_node = cur_node.next
            if cur_idx==index:
                last_node.next = cur_node.next
                return 
            cur_idx +=1       

myList= LinkList()

myList.append(0)
myList.append(1)
myList.append(2)
myList.append(3)
myList.append(4)

myList.display()

myList.erase(1)
myList.display()
print("element at 2nd index: %d"% myList.get(2))


