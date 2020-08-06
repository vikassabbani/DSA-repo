graph = {
        1: [2, 3, 4],
        2: [5, 6],
        3: [6],
        4: [7],
        5: [],
        6: [],
        7: []}

def bfs(graph, start, end):
    queue = []
    queue.append([start])
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node == end:
            return path
        for i in graph[node]:
            npath = list(path)
            npath.append(i)
            queue.append(npath)

print(bfs(graph, 1, 6))