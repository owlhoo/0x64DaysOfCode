from collections import deque

# fastest queue operations in python


def bfs(graph, root):
    distances = {root: 0}
    q = deque([root])
    while q:
        current = q.pop()
        for neighbour in graph[current]:
            if neighbour not in distances:
                distances[neighbour] = distances[current] + 1
                q.append(neighbour)
    return distances


graphino = {1: [2, 3], 2: [4], 3: [4, 5], 4: [3, 5], 5: []}
print(bfs(graphino, 1))



