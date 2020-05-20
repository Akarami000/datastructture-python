from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph=defaultdict(list)

    def addEdge(self,u,v):
            self.graph[u].append(v)

    def DEFdefal(self,v,visted):
        visted[v]=True
        print(v, end=" ")

        for i in self.graph[v]:
            if visted[i]== False:
                self.DEFdefal(i,visted)


    def DFS(self):
        visted=[False]*(len(self.graph))

        for i in self.graph:
             if visted[i]==False:
                 self.DEFdefal(i,visted)            


g = Graph() 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3) 
  
print ("Following is Depth First Traversal")
g.DFS() 