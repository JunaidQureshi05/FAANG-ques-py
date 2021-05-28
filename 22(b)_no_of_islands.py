#Breadth first approach
#O(m*n) Time | O(max(m,n)) Space
def no_of_islands(matrix):
    sizes = []
    visited = [[False for value in row] for row in matrix]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if visited[i][j]:
                continue
            traverseNode(i,j,matrix,visited,sizes)
    return len(sizes)

def traverseNode(i,j,matrix,visited,sizes):
    currentIslandSize = 0
    nodesToExplore =[[i,j]]
    while len(nodesToExplore):
        currentNode = nodesToExplore.pop()
        i=currentNode[0]
        j=currentNode[1]
        if visited[i][j]:
            continue
        visited[i][j] = True
        if matrix[i][j]=="0":
            continue
        currentIslandSize+=1
        unVisitedNeighbours = getUnVisitedNeighbours(i,j,matrix,visited)
        for neighbour in unVisitedNeighbours:
            nodesToExplore.append(neighbour)
    if currentIslandSize>0:
        sizes.append(currentIslandSize)

def getUnVisitedNeighbours(i,j,matrix,visited):
    neighbours=[]
    if i>0 and not visited[i-1][j]:
        neighbours.append([i-1,j])
    if i<len(matrix)-1 and not visited[i+1][j]:
        neighbours.append([i+1,j])
    if j>0 and not visited[i][j-1]:
        neighbours.append([i,j-1])
    if j<len(matrix[0])-1 and not visited[i][j+1]:
        neighbours.append([i,j+1])
    return neighbours
print(no_of_islands([
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]])
    )   