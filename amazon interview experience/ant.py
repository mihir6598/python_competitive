# https://www.geeksforgeeks.org/amazon-interview-experience-for-sde-1-amazon-wow-drive/
from collections import defaultdict
class Graph():
    def __init__(self):
        self.graph = defaultdict(list)
    def add(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)
       


    def check(self):
        visited = {}

        for i in self.graph.keys():
            visited[i] = -1
            start = i
        
        q = [i]
        visited[i] = 1
        while q:
            u = q.pop()
            for v in self.graph[u]:
                if visited[v] == -1:
                    q.append(v)
                    visited[v] = 1-visited[u]
                elif visited[v] == visited[u]:
                    return False
        return True


if __name__ == "__main__":
    arr = ["1-2", "3-4", "5-6"]
    family = Graph()
    for i in arr:
        temp = i.split("-")
        family.add(temp[0],temp[1])
    print (family.check())
    