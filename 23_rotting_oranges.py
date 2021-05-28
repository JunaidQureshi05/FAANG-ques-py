#O(n) Time | O(n) Space
directions = [[-1,0],[1,0],[0,-1],[0,1]]
def oranges_rotting(matrix):
    EMPTY,FRESH,ROTTEN=0,1,2
    queue = []
    freshOranges = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if(matrix[i][j]==ROTTEN):
                queue.append([i,j])
            if matrix[i][j]==FRESH:
                freshOranges +=1
    minutes=0
    currentQueueSize = len(queue)
    while len(queue)>0:
        if currentQueueSize==0:
            currentQueueSize=len(queue)
            minutes+=1
        currentOrange = queue.pop(0)
        currentQueueSize-=1
        row = currentOrange[0]
        col=currentOrange[1]

        for i in range(len(directions)):
            currentDirection = directions[i]
            nextRow=row+currentDirection[0]
            nextCol=col+currentDirection[1]
            if nextRow<0 or nextCol<0 or nextRow>=len(matrix) or nextCol>=len(matrix[0]):
                continue
            if(matrix[nextRow][nextCol]==FRESH):
                matrix[nextRow][nextCol]=ROTTEN
                freshOranges-=1
                queue.append([nextRow,nextCol])
    if freshOranges!=0:
        return -1
    return minutes
        
print(oranges_rotting([[0,2]]))