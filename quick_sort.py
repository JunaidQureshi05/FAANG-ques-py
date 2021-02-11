# quick_sort.py
def quickSortHelper(array,start,end):
    if start >= end:
        return 
    pivot = start
    left = start+1
    right =end 

    while left <= right:
        if  array[left] > array[pivot] and array[right] < array[pivot]:
            swap(array,left,right)
            left+=1
            right-=1   
        if array[left] <= array[pivot]:
            left+=1
        if array[right] >= array[pivot]:
            right-=1   

    swap(array,right,pivot)
    leftSubArrayIsSmall = right-1 - start < end -(right+1)
    if leftSubArrayIsSmall:
        quickSortHelper(array,start,right-1)
        quickSortHelper(array,start+1,end)
    else:
        quickSortHelper(array,start+1,end)    
        quickSortHelper(array,start,right-1)





def quickSort(array):
    quickSortHelper(array,0,len(array)-1)
    return array
def swap(array,a,b):
    array[a],array[b] =array[b],array[a]

