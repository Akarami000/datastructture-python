

#https://www.geeksforgeeks.org/top-algorithms-and-data-structures-for-competitive-programming/
###########################defaultdict############
# from collections import defaultdict

# def val():
#     return "not present"


# d=defaultdict(val)
# d["a"]=1
# d['b']=2 

# print(d['a'])
# print(d['b'])
# print(d['c'])


############################passing list class
# from collections import defaultdict 
  
  
# # Defining a dict 
# d = defaultdict(list) 
  
# for i in range(5): 
#     d[i].append(i) 
      
# print("Dictionary with values as list:") 
# print(d) 

##################################
from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph=defaultdict(list)
      
    def addEdge(self,u,v):
        self.graph[u].append(v)

    def BFS(self,s):
        vist=[False]*(len(self.graph)) 

        queue=[]

        queue.append(s)
        vist[s]=True

        while queue:
            s = queue.pop(0)
            print(s,end = " ")

            for i in self.graph[s]:
                if vist[i]==False:
                    queue.append(i)
                    vist[i]=[True]






g=Graph()
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3) 

g.BFS(2)


