# O(n) Time | O(n) Space
def maxDepth(root,currentDepth=0):
    if not root:
        return currentDepth
    currentDepth +=1
    return max(maxDepth(root.left,currentDepth),maxDepth(root.right,currentDepth))    

    
insert([1,1,1,1,None,None,None,1,None,None,None,1,None,None])
print(maxDepth(root,0))