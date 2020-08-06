import numpy as np


class Graph:

    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_matrix = np.zeros((vertices, vertices))
        self.visited = [0] * self.vertices

    def addedge(self, u, v, w=1):
        self.adj_matrix[u][v] = w

    def removeedge(self, u, v):
        self.adj_matrix[u][v] = 0

    def DFS(self, source):
        if self.visited[source] == 0:
            print(source, end="-->")
            self.visited[source] = 1
            for j in range(self.vertices):
                if self.adj_matrix[source][j] == 1 and self.visited[j] == 0:
                    self.DFS(j)


l = Graph(7)
l.addedge(0, 1)
l.addedge(0, 5)
l.addedge(0, 6)
l.addedge(1, 0)
l.addedge(1, 5)
l.addedge(1, 2)
l.addedge(1, 6)
l.addedge(2, 3)
l.addedge(2, 4)
l.addedge(2, 6)
l.addedge(3, 4)
l.addedge(4, 2)
l.addedge(4, 5)
l.addedge(5, 2)
l.addedge(5, 3)
l.addedge(6, 3)
l.DFS(0)
