# O(n^2) Time | O(1) Space 
# Brute Force Approach
def pair_with_sum_1(array,target):
	for i in range(len(array)):
		for j in range(i+1,len(array)):
			if array[i] + array[j] ==target:
				return [i,j]
	return []



# Optimized

def pair_with_sum(array,target):
	memoize ={}

	for i in range(len(array)):
		potentialMatch = target - array[i]
		if potentialMatch in memoize:
			return [memoize[potentialMatch],i]
		else:
			memoize[array[i]] = i
	return []

print(pair_with_sum([1,3,9,2],11))   				