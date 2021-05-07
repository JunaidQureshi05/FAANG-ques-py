# O(n) Time | O(d) Space Where d is the depth of BST(Binary search tree)

def validate_binary_search_tree_helper(node,min,max):
    if node.value >=max or node.value <=min:
        return False
    if node.left:
        if not validate_binary_search_tree(node.left, min, node.value):
            return False
    if node.right:
        if not validate_binary_search_tree(node.right, node.value, max):
            return False
    return True                

def is_valid_bst(root):
    if not root:
        return True
    return validate_binary_search_tree_helper(root, float('-inf'), float('inf'))       