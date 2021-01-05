# O(n) Time | O(1) Space
def flatten(head):
    if head is None:
        return None
    currentNode = head
    while currentNode != None:
        if currentNode.child == None:
            currentNode = currentNode.next
        else:
            tail = currentNode.child
            while tail.next != None:
                tail =tail.next
            tail.next = currentNode.next
            if currentNode.next != None:
                tail.next.prev = tail
            currentNode.next = currentNode.child
            currentNode.next.prev = currentNode 
            currentNode.child = None
    return head                 




