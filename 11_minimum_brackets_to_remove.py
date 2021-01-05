# O(n) Time | O(n) Space
def split(string):
	return [char for char in string]
def minimum_remove_to_make_valid(string):
	res = split(string)
	print(res)
	stack = []
	for i in range(len(res)):
		if res[i] =="(":
			stack.append(i)
		elif res[i] == ')' and len(stack):
			stack.pop()
		elif res[i] ==")":
			res[i] = ''
					
	while len(stack) !=0:
		current_idx = stack.pop()
		res[current_idx] = ''	
	
	return  ''.join(res)				

print(minimum_remove_to_make_valid('))(('))    


