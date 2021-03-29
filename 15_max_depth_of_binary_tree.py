# O(n) Time | O(n) Space
def maxDepth(root,currentDepth=0):
    if not root:
        return currentDepth
    currentDepth +=1
    return max(maxDepth(root.left,currentDepth),maxDepth(root.right,currentDepth))    

print(maxDepth(root,0))
