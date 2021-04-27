def right_side_of_tree(root):
    results = []
    DFS(root,0,results)
    return results

def DFS(node,currentLevel,results):
    if not node:
        return
    if currentLevel >= len(results):
        results.append(node.val)
    if node.right:
        DFS(node.right,currentLevel+1,results)    
    if node.left:
        DFS(node.left,currentLevel+1,results)    
