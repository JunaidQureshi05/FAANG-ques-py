# Function to implement binary search
# O(log(n)) Time | O(1) Space
def binary_search(start,end,array,item):
    low = start
    high = end
    mid = (low+high)//2
    while low<=high:
        if array[mid] == item:
            return mid
        elif array[mid] > item:
            high = mid - 1
        else:
            low = mid+1
        mid = (low+high)//2
    return -1     



# O(logn) Time | O(1) Space
# Function to search range
def search_range(array,element):
    if not len(array):
        return [-1,-1]
    first_pos = binary_search(0,len(array)-1,array,element)
    if first_pos ==-1:
        return [-1,-1]
    start_pos,end_pos=first_pos,first_pos

    while start_pos != -1:
        temp1 = start_pos
        start_pos = binary_search(0,start_pos-1,array,element)
    start_pos = temp1

    while end_pos!=-1:
        temp2 = end_pos
        end_pos=binary_search(end_pos+1,len(array)-1,array,element)    
    end_pos = temp2

    return [start_pos,end_pos]    

print(search_range([1,2,4,4,5,5,5,5,10],5))