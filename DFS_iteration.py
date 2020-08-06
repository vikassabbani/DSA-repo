import numpy as np


class Grap:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_matrix = np.zeros((vertices, vertices))
        self.visited = [False] * self.vertices

    def addedge(self, u, v, w=1):
        self.adj_matrix[u][v] = w

    def dfs_it(self, i):
        s = []
        s.append(i)
        self.visited[i] = True
        while len(s) > 0:
            u = s[-1]
            s.pop()
            print(u)
            for v in range(self.vertices):
                if self.adj_matrix[u][v] == 1 and self.visited[v] == False:
                    s.append(v)
                    self.visited[v] = True

    def dfs(self):
        for i in range(self.vertices):
            if not self.visited[i]:
                self.dfs_it(i)

    def display(self):
        print(self.adj_matrix)


g = Grap(7)
g.addedge(0, 1)
g.addedge(0, 5)
g.addedge(0, 6)
g.addedge(1, 0)
g.addedge(1, 5)
g.addedge(1, 2)
g.addedge(1, 6)
g.addedge(2, 3)
g.addedge(2, 4)
g.addedge(2, 6)
g.addedge(3, 4)
g.addedge(4, 2)
g.addedge(4, 5)
g.addedge(5, 2)
g.addedge(5, 3)
g.addedge(6, 3)
g.dfs()
