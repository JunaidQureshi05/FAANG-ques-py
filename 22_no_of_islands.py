#Depth First Search Approach
#O(n^2) Time | O(n) Space
def no_of_islands(matrix):
    noOfIslands=0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] =="1":
                noOfIslands+=1
                DFS(i,j,matrix)
    return noOfIslands

# Funtion for depth first search
def DFS(i,j,matrix):
    if i< 0 or i>= len(matrix) or j<0 or j>= len(matrix[i]) or matrix[i][j]=="0":
        return
    matrix[i][j]="0"
    print(i,j)
    DFS(i-1,j,matrix)
    DFS(i+1,j,matrix)
    DFS(i,j-1,matrix)
    DFS(i,j+1,matrix)

print(no_of_islands( [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]])
    )