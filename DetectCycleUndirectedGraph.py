from collections import defaultdict


class Graph:

    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = defaultdict(list)
        self.visited = [False] * self.vertices

    def addEdge(self, v, w):
        self.graph[v].append(w)
        self.graph[w].append(v)

    def checkcyclc(self, v, parent):
        self.visited[v] = True
        for i in self.graph[v]:
            if self.visited[i] == False:
                if self.checkcyclc(i, v):
                    return True
            elif parent != i:
                return True
        return False

    def isCyclic(self):
        for i in range(self.vertices):
            if self.visited[i] == False:
                if self.checkcyclc(i, -1) == True:
                    return True
        return False


g = Graph(2)
g.addEdge(0, 1)
g.addEdge(1, 2)
g.addEdge(2, 3)
g.addEdge(3, 0)
print(g.isCyclic())

