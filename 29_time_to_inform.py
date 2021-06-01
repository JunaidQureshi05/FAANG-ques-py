managersArray = [2, 2, 4, 6, -1, 4, 4, 5];
informTimeArray = [0, 0, 4, 0, 7, 3, 6, 0];


def min_time_to_inform(n,headID,managers,informationTime):
    adjList = list(map(lambda x:[],managers))
    for i in range(n):
        manager = managers[i]
        if manager==-1:
            continue
        adjList[manager].append(i)
    return DFS(headID,adjList,informationTime)

def DFS(currentID,adjList,informationTime):
    if len(adjList[currentID])==0:
        return 0
    Max=0
    subordinates = adjList[currentID]
    for i in range(len(subordinates)):
        Max = max(Max,DFS(subordinates[i],adjList,informationTime))
    return Max + informationTime[currentID]

print(min_time_to_inform(8,4,managersArray,informTimeArray))