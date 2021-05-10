# Direction of depth first search up => right => down => =>left

testMatrix = [
  [1, 2, 3, 4, 5],
  [6, 7, 8, 9, 10],
  [11, 12, 13, 14, 15],
  [16, 17, 18, 19, 20]
];

directions = [
  [-1, 0], 
  [0, 1], 
  [1, 0], 
  [0, -1] 
]

def array_traversal_dfs(array):
    seen = [[False for y in range(len(array[0]))] for x in range(len(array))]
    values =[]
    dfs(array,0,0,seen,values)
    return values

def dfs(matrix,row,col,seen,values):
    if row<0 or col <0 or row >=len(matrix) or col >=len(matrix[0]) or seen[row][col]:
        return
    values.append(matrix[row][col])
    seen[row][col] = True
    for i in range(len(directions)):
        current_direction = directions[i]
        dfs(matrix, row+current_direction[0], col+current_direction[1], seen, values)



print(array_traversal_dfs(testMatrix) )   