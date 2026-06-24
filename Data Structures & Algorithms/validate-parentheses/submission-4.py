class Solution:
    def isValid(self, s: str) -> bool:
        #Brute force try 2
        stack = []

        for ch in s:
            if ch == '(' or ch == '[' or ch =='{':
                stack.append(ch)
                continue
            else:
                if len(stack) == 0:
                    return False
            
            if ch == ')' and stack[-1] == '(':
                stack.pop()
            elif ch == ']' and stack[-1] == '[':
                stack.pop()
            elif ch == '}' and stack[-1] == '{':
                stack.pop()
            else:
                return False
            
        if len(stack) == 0:
            return True
        else:
            return False
        