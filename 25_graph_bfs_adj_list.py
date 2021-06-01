adjacencyList = [
  [1, 3],
  [0],
  [3, 8],
  [0, 2, 4, 5],
  [3, 6],
  [3],
  [4, 7],
  [6],
  [2]
]



def BFS(graph):
    seen={}
    values=[]
    queue=[0]
    while len(queue):
        vertex = queue.pop(0)
        values.append(vertex)
        seen[vertex]= True
        connections = graph[vertex]
        for i in range(len(connections)):
            if connections[i] not in seen:
                queue.append(connections[i])
    return values

print(BFS(adjacencyList))