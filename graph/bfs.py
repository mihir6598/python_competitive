from collections import defaultdict

class graph:
    def __init__(self):
        self.graph = defaultdict(list)
    def add(self,u,v):
        self.graph[u].append(v)
    def bfs(self,s):
        visited = [False] * (max(self.graph) + 1)
        queue = []
        queue.append(s)
        visited[s] = True
 
        while queue:

            s = queue.pop(0)
            print (s, end = " ")
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

g = graph()
g.add(0, 1)
g.add(0, 2)
g.add(1, 2)
g.add(2, 0)
g.add(2, 3)
g.add(3, 3)
 
print ("Following is Breadth First Traversal"
                  " (starting from vertex 2)")
g.bfs(2)