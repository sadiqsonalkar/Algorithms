from collections import defaultdict
class Graph:
    def __init__(self,vertices):
        self.V=vertices
        self.graph=defaultdict(list)
    def addEdge(self,n1,n2):
        self.graph[n1].append(n2)
    def isReachable(self,s,d):
        visited=[False]*(self.V)
        queue=[]
        queue.append(s)
        visited[s]=True

        while queue:
            n=queue.pop(0)
            if n==d:
                return True
            for i in self.graph[n]:
                if visited[i]==False:
                    queue.append(i)
                    visited[i]=True
        return False
g = Graph(4)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

n1=2; n2=3

if g.isReachable(n1,n2):
    print("There is a path from %d to %d" %(n1,n2))
else:
    print("There is no path from %d to %d" %(n1,n2))
n1=3; n2=2
if g.isReachable(n1,n2):
    print("There is a path from %d to %d" %(n1,n2))
else:
    print("There is no path from %d to %d" %(n1,n2))
