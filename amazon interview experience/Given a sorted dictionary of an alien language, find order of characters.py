# https://www.geeksforgeeks.org/given-sorted-dictionary-find-precedence-characters/
from collections import defaultdict
class Graph():
    def __init__(self):
        self.graph = {}
    def add(self,u,v):
        if u in self.graph:
            if v in self.graph and u in self.graph[v]:
                pass
            elif v not in self.graph[u]:
                self.graph[u].append(v)
        else:
            self.graph[u] = [v]
    def dfsutil(self,u,visited,stack):
        visited.add(u)
        if u in self.graph:
            for i in self.graph[u]:
                if i not in visited:
                    self.dfsutil(i,visited,stack)
        stack.append(u)
        print (stack)
    
    def topological(self):
        visited = set()
        stack = []
        print (self.graph)
        for i in self.graph.keys():
            if i not in visited:
                self.dfsutil(i,visited,stack) 
        return stack[::-1]
        
def solve(arr):
    language = Graph()
    for i in range(len(arr)-1):
        word1 = arr[i]
        word2 = arr[i+1]
        for j in range((min(len(word1),len(word2)))):
            if word2[j] != word1[j]:
                language.add(word1[j],word2[j])
    return language.topological()
    
        

if __name__ == "__main__":
    arr = ["baa", "abcd", "abca", "cab", "cad"]
    print (solve(arr))