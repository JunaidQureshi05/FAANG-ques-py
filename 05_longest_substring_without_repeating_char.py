# Brute Force Approach 
# O(n^2) Time | O(n) Space
def longest_substring(string):
    if len(string) <=1:
        return len(string)
    longest_length =0
    for i in range(len(string)):
        seen_chars ={}
        current_length = 0
        for j in range(len(string)):
            if string[j] not in seen_chars:
                seen_chars[string[j]] =True
                current_length +=1
                longest_length = max(longest_length,current_length)
            else:
                break
    return longest_length               

print(longest_substring('abeefgh'))    


# Optimized approach

def longest_substring_2(s):
    longest_length = 0
    seen_chars = {}
    left = 0
    for right in range(len(s)):
        current_char = s[right]
        previousSeenChar = seen_chars.get(current_char,-1)
        if previousSeenChar >= left:
            left = previousSeenChar +1
        seen_chars[current_char] = right
        longest_length = max(longest_length,right-left+1)    
    return longest_length    


print(longest_substring_2('abcabcbb'))    