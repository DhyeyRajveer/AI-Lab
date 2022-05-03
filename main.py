from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def BFS(self, s):
        visited = [False] * len(self.graph)
        queue = [s]
        visited[s] = True
        while queue:
            temp = queue.pop(0)
            print(temp, end=' ')
            for child in self.graph[temp]:
                if not visited[child]:
                    queue.append(child)
                    visited[child] = True

    def DFS(self, s):
        visited = set()
        self.DFSUtil(s, visited)

    def DFSUtil(self,s,visited):
        print(s, end=" ")
        visited.add(s)
        for child in self.graph[s]:
            if child not in visited:
                self.DFSUtil(child, visited)


g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print("Following is Breadth First Traversal", "(starting from vertex 2)")
g.BFS(2)
