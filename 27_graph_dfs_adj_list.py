adjecencyList=[ [1, 3],
  [0],
  [3, 8],
  [0, 2, 4, 5],
  [3, 6],
  [3],
  [4, 7],
  [6],
  [2]
];


def DFS(vertex,graph,values,seen):
    values.append(vertex)
    seen[vertex] = True
    connections=graph[vertex]
    for i in range(len(connections)):
        connection= connections[i]
        if connection not in seen:
            DFS(connection,graph,values,seen)
    return values

print(DFS(0,adjecencyList,[],{}))