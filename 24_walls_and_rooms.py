#O(n) Time | O(n) Space
WALL = -1
GATE = 0
INF = 2147483647

def DFS(row,col,matrix,count):
    if row<0 or col<0 or row>=len(matrix)or col>=len(matrix[0]) or count>matrix[row][col]:
        return 
    matrix[row][col]= count
    DFS(row -1,col,matrix,count+1)
    DFS(row+1,col,matrix,count+1)
    DFS(row,col-1,matrix,count+1)
    DFS(row,col+1,matrix,count+1)

def walls_and_gates(matrix):
    count=0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j]==GATE:
                DFS(i,j,matrix,count)
    return matrix


print(walls_and_gates([
  [INF, -1, 0, INF],
  [INF, INF, INF, 0],
  [INF, -1, INF, -1],
  [0, -1, INF, INF]
]))