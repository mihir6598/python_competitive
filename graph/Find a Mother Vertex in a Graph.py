from collections import defaultdict

class graph:
    def __init__(self,v):
        self.graph = defaultdict(list)
        self.v = v
    
    def bfs(self,visited,v):
        visited.add(v)
        for i in self.graph[v]:
            if i not in visited:
                visited.add(i)
                self.bfs(visited,i)

    def add(self,u,v):
        self.graph[u].append(v)
    
    def mother(self):
        visited = set()
        for i in range(self.v):
            print (visited)
            if i not in visited:
                self.bfs(visited,i)
                ans = i
        return ans
g = graph(7)
g.add(0, 1)
g.add(0, 2)
g.add(1, 3)
g.add(4, 1)
g.add(6, 4)
g.add(5, 6)
g.add(5, 2)
g.add(6, 0)
print (g.mother())


