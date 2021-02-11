from quick_sort import quickSort
# O(nlogn(n)) | O(log(n) Space
def kth_largest_element(array,k):
	array  = quickSort(array)
	array.reverse()	
	return array[k-1]

print(kth_largest_element([3,2,1,5,6,4],2))