# BrutForce Approach

# O(n^2) Time | O(n) Space
def get_traped_rain_water(heights):
    total_water = 0
    for i in range(len(heights)):
        left,right,left_max,right_max = i,i,0,0
        while left >=0:
            left_max =  max(left_max,heights[left])
            left-=1
        while right < len(heights):
            right_max = max(right_max,heights[right])
            right+=1
        current_water = min(left_max,right_max) - heights[i]
        if current_water >=0:
            total_water += current_water
    return total_water                  
print(get_traped_rain_water([0, 1, 0, 2, 1, 0, 3, 1, 0, 1, 2]))    


# Optimized way
# O(n) Time | O(1) Space
def get_traped_rain_water_2(heights):
    left,right,left_max,right_max=0,len(heights)-1,0,0
    total_water =0
    while(left< right):
        if(heights[left]<=heights[right]):
            if heights[left] >= left_max:
                left_max = heights[left]
            else:
                total_water += left_max - heights[left]
            left +=1    
        else:
            if heights[right] >= right_max:
                right_max = heights[right]
            else:
                total_water += right_max -heights[right]
            right-=1
    return total_water        

print(get_traped_rain_water_2([0, 1, 0, 2, 1, 0, 3, 1, 0, 1, 2]))    