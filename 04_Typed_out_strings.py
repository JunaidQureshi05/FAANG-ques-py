

# BrutForce Approach
# O(a+b) Time | O(a+b) Time
def final_string(string):
    array = []
    for i in range(len(string)):
        if string[i] != '#':
            array.append(string[i])
        else:
            if len(array) !=0:
                array.pop()
    return ''.join(array)           

def back_space_compare(str1,str2):
    finalStr1,finalStr2  =final_string(str1),final_string(str2) 
    if len(finalStr1) != len(finalStr2):
        return False
    else:
        for i in range(len(finalStr1)):
            if finalStr1[i] != finalStr2[i]:
                return False
    return True            



# print(back_space_compare('adcf#ff','adq#cff'))    


# Optimized solution

def  back_space_compare_2(S,T):
    p1,p2= len(S) - 1, len(T) -1
    while p1 >= 0 or p2 >= 0:
        if S[p1] == '#' or T[p2] =='#':
            if S[p1] =='#':
                counter=2
                while counter > 0:
                    counter -=1
                    p1 -=1
                    # cehck if S is over
                    if p1 ==-1:
                        # check if T is also over
                        if T[p2] =='#':
                            counter=2
                            while counter > 0:
                                counter-=1
                                p2-=1
                                if p2==-1:
                                    return True
                                if T[p2] =='#':
                                    counter+=2
                        return False    

                    if p1==-1:
                        if p2 >=0:
                            return False
                        else:
                            return True    
                    if S[p1] =='#':
                        counter+=2    
                              
            if T[p2] == '#':
                if T[p2] =='#':
                    counter=2
                    while counter > 0:
                        counter-=1
                        p2-=1
                        if p2==-1:
                            return True
                        if T[p2] =='#':
                            counter+=2
        else:
            if S[p1] != T[p2]:
                return False
            else:
                p1-=1
                p2-=1
    return True                                          

print(back_space_compare_2('a#b#','c#d#'))    
    