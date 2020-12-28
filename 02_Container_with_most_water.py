
# Brutfore approach
 
# O(n ^ 2) Time | O(1) Space
def container_with_max_water_1(array):
    maxContainedWater = 0
    for i in range(len(array)):
        for j in range(i+1,len(array)):
            height = min(array[i],array[j])
            width = j - i
            containedWater=height*width
            maxContainedWater = max(maxContainedWater,containedWater)
    return maxContainedWater        

print(container_with_max_water_1([1,8,6,2,5,4,8,3,7]))  

# Optimized
# O(n) Time | O(1) Space
def container_with_max_water_2(array):
    left,right = 0, len(array)-1
    maxWater  = 0
    while left < right:
        height = min(array[left],array[right])
        width = right - left
        maxWater = max(maxWater,height*width)
        if array[left] < array[right]:
            left+=1
        else:
            right-=1
    return maxWater             
print(container_with_max_water_2([1,8,6,2,5,4,8,3,7]))