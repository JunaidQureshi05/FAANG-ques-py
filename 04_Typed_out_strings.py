

# BrutForce Approach
def final_string(string):
    array = []
    for i in range(len(string)):
        if string[i] != '#':
            array.append(string[i])
        else:
            if len(array) !=0:
                array.pop()
    return ''.join(array)           

def bac_space_compare(str1,str2):
    finalStr1,finalStr2  =final_string(str1),final_string(str2) 
    if len(finalStr1) != len(finalStr2):
        return False
    else:
        for i in range(len(finalStr1)):
            if finalStr1[i] != finalStr2[i]:
                return False
    return True            



print(bac_space_compare('adcf#ff','adq#cff'))    