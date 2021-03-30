from collections import defaultdict

class graph():
    def __init__(self,v):
        self.v = v
        self.graph = defaultdict(list)
    
    def addEdge(self,u,v):
        self.graph[u].append(v)
    
    def checkCycle(self,u,visited,stack):
        visited[u] = True
        stack[u] = True

        for i in self.graph[u]:
            if visited[i] == False:
                if self.checkCycle(i,visited,stack):
                    return True
            elif stack[u]:
                return True
        stack[u] = False

    def dfs(self):
        visited = [False]*self.v
        stack = [False]*self.v

        for i in range(self.v):
            if not visited[i]:
                if self.checkCycle(i,visited,stack):
                    return True
        return False


if __name__ == "__main__":
    g = graph(4) 
    g.addEdge(0, 1) 
    g.addEdge(0, 2) 
    g.addEdge(1, 2) 
    g.addEdge(2, 0) 
    g.addEdge(2, 3) 
    g.addEdge(3, 3) 
    print (g.dfs())