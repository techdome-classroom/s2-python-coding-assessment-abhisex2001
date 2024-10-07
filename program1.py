def isValid(s: str) -> bool:
   
    bracket_map = {')': '(', '}': '{', ']': '['}
    stack = []

    for char in s:
        if char in bracket_map.values():  
            stack.append(char)
        elif char in bracket_map:  
            if not stack or stack.pop() != bracket_map[char]:  
                return False

    

# Example :
print(isValid("()"))       
print(isValid("()[]{}"))   
print(isValid("(]"))       








    



  

