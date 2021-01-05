# O(n)Time | O(1) Space
def reverse_a_linked_list(head):
	previous = None
	currentNode = head
	while currentNode:
		nextNode = currentNode["next"]
		currentNode["next"] = previous
		previous = currentNode
		currentNode = nextNode
	return previous	



linked_list = {
	'value':5,
	'next':{
	'value':6,
	'next':{
	'value':7,
	'next':None
	}
	}
}

print(reverse_a_linked_list(linked_list))