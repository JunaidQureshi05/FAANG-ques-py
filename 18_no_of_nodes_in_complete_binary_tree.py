# O(h^2+h)=>O(h) Time where h is height of tree
# O(1) =>Space
import math
def get_tree_height(root):
    height=0
    while root:
        root=root.left
        height+=1
    return height    

def node_exits(index_to_find,height,node):
    left = 0
    right = pow(2,height)-1
    count = 0
    while(count<height):
        mid_of_node = math.ceil((left+right)/2)
        if(index_to_find>= mid_of_node):
            node = node.right
            left = mid_of_node
        else:
            node = node.left
            right =mid_of_node-1
        count+=1
    return node !=None            


def count_node(tree):
    if not root:
        return 0
    height = get_tree_height(root)
    if height==0:
        return 1
    upper_count = pow(2,height)-1
    left = 0
    right = upper_count
    while left<right:
        index_to_find = math.ceil((left+right)/2)
        if(node_exist(index_to_find,hright,root)):
            left = index_to_find
        else:
            right = index_to_find-1      
    return upper_count+left+1

    