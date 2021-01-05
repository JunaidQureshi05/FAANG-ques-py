# O(n) Time | O(n) Space
def valid_parantheses(string):
    if string =='':
        return True
    stack = []
    opening ='[{('
    closing = ']})'
    matching_parentheses = {
    '}':'{',
    ']':'[',
    ')':'('
    }

    for char in string:
        if char in opening:
            stack.append(char)
        elif char in closing:
            if len(stack) == 0:
                return False
            elif stack[-1] == matching_parentheses[char]:
                stack.pop()
            else:
                return False
    return True

print(valid_parantheses('{()[]}'))                                    