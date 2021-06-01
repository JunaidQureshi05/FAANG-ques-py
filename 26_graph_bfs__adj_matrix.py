adjacencyMatrix = [
  [0, 1, 0, 1, 0, 0, 0, 0, 0],
  [1, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 1, 0, 0, 0, 0, 1],
  [1, 0, 1, 0, 1, 1, 0, 0, 0],
  [0, 0, 0, 1, 0, 0, 1, 0, 0],
  [0, 0, 0, 1, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 1, 0, 0, 1, 0],
  [0, 0, 0, 0, 0, 0, 1, 0, 0],
  [0, 0, 1, 0, 0, 0, 0, 0, 0]
]

def BFS(graph):
    seen ={}
    queue = [0]
    values = []
    while len(queue):
        vertex =queue.pop(0)
        values.append(vertex)
        seen[vertex] = True
        connections = graph[vertex]
        for i in range(len(connections)):
            if i not in seen and connections[i]>0:
                queue.append(i)
    return values

    
print(DFS(adjacencyMatrix))