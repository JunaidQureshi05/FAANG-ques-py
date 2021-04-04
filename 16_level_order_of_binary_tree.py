def level_order_of_binary_tree(root):
    if not root:
        return []
    queue = [root]
    result = []
    length = len(queue) ,count= 0 
    while len(queue):
        current_level_values = []
        current_node = queue.pop(0)
        while(count < length):
            current_level_values.append(current_node.value)
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
            count+=1
        result.append(current_level_values)
    return result    