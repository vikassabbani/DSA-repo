from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.vertices = vertices
        self.visited = [False] * self.vertices

    def addedge(self, u, v):
        self.graph[u].append(v)

    def checkcycle(self, v):
        self.visited[v] = True
        for neighbour in self.graph[v]:
            if not self.visited[neighbour]:
                if self.checkcycle(neighbour):
                    return True
            elif self.visited[neighbour]:
                return True
        self.visited[v] = False
        return False

    def iscyclic(self):
        for node in range(self.vertices):
            if not self.visited[node]:
                if self.checkcycle(node):
                    return True
        return False


g = Graph(5)
g.addedge(0, 1)
g.addedge(1, 2)
g.addedge(2, 3)
g.addedge(2, 4)
g.addedge(4, 3)
print(g.iscyclic())
