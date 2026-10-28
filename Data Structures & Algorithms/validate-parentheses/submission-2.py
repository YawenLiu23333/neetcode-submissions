class Solution:
    def isValid(self, s: str) -> bool:
        opentoclose = {')':'(', ']':'[', '}':'{'}
        stack = []
        for l in s:
            if stack and l in opentoclose:
                if opentoclose[l] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(l)
        
        if not stack:
            return True
        else:
            return False

            