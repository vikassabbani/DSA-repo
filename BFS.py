from queuee import queue
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

    def BFS(self, source):
        i = source
        q = queue()
        visited = [0] * self.vertices
        print(i, end="-->")
        visited[i] = 1
        q.enqueue(i)
        while not q._isempty():
            i = q.dequeue()
            for j in range(self.vertices):
                if self.adj_matrix[i][j] == 1 and visited[j] == False:
                    print(j, end="-->")
                    visited[j] = 1
                    q.enqueue(j)

    def display(self):
        print(self.adj_matrix)


g = Graph(7)
g.addedge(0, 1)
g.addedge(0, 5)
g.addedge(0, 6)
g.addedge(1, 0)
g.addedge(1, 2)
g.addedge(1, 5)
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

g.BFS(0)
