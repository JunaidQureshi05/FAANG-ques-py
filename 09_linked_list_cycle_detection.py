# O(n) Time | O(n) Space
# Naive approach
def find_cycle(head):
	currentNode = head
	seenNodes = set()
	while currentNode not in seenNodes:
		if currentNode.next == None:
			return False
		seenNodes.add(currentNode)
		currentNode = currentNode.next
	return currentNode	

# Floyed tortoise method

def find_cycle_2(head):
	if not head:
		return None
	tortoise=head
	hare = head

	while True:
		tortoise = tortoise.next
		hare = hare.next
		if hare == None or hare.next == None:
			return None

		else:
			hare =hare.next
		if hare == tortoise:
			break
    p1=head
    p2 = tortoise
    while p1!=p2:
    	p1 = p1.next
    	p2 = p2.next
    return p2	