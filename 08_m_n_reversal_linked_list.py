linked_list = {
	'value':1,
	'next':{
	'value':2,
	'next':{
	'value':3,
	'next':{
	'value':4,
	'next':{
	'value':5,
	'next':None
	}
	}
	}
	}
}

def reverse_between_m_n(head,m,n):
	current_pos =1
	currentNode =head
	while current_pos < m:
		start =currentNode
		currentNode =currentNode['next']
		current_pos+=1
	new_list =None
	tail = currentNode
	while current_pos >=m and current_pos<=n:
		nextNode = currentNode['next']
		currentNode['next'] = new_list
		new_list =currentNode
		currentNode= nextNode
		current_pos+=1
	start['next'] = new_list
	tail['next'] = currentNode

	if m>1:
		return head
	else:
		return new_list		

print(reverse_between_m_n(linked_list,2,4))



#  1 -- 2 -- 3 --4 --5
#  1 __ 4 __ 3 __ 2 __5
