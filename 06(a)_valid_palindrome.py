# O(n) Time | O(n) Space
def isPalindrome(s: str) -> bool:
    string = ''.join([i for i in s if i.isalnum()]).lower()
    left = 0
    right = len(string) - 1
    while left<right:
        if string[left] != string[right]:
            return False
        left+=1
        right-=1
    return True

print(isPalindrome('A man, a plan, a canal: Panama'))    