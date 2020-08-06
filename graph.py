import numpy as np

class Graph:

    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_matrix = np.zeros((vertices, vertices))

    def addedge(self, u, v, w=1):
        self.adj_matrix[u][v] = w

    def removeedge(self, u, v):
        self.adj_matrix[u][v] = 0

    def countedge(self):
        count = 0
        for i in range(self.vertices):
            for j in range(self.vertices):
                if not self.adj_matrix[i][j] == 0:
                    count += 1
        return count

    def countvetices(self):
        return self.vertices

    def getedge(self, u, v):
        return self.adj_matrix[u][v]

    def indegree(self, u):
        count = 0
        for i in range(self.vertices):
            if self.adj_matrix[i][u] == 1:
                count += 1
        return count

    def outdegree(self, u):
        count = 0
        for i in range(self.vertices):
            if self.adj_matrix[u][i] == 1:
                count += 1
        return count

    def display(self):
        print(self.adj_matrix)


l = Graph(7)
l.addedge(0, 1)
l.addedge(0, 5)
l.addedge(0, 6)
l.addedge(1, 0)
l.addedge(1, 2)
l.addedge(1, 5)
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
l.display()