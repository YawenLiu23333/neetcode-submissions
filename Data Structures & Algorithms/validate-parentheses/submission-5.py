class Solution:
    def isValid(self, s: str) -> bool:
        check = {')':'(', ']':'[', '}':'{'}
        stack = []
        for p in s:
            if p in check:
                if not stack or check[p] != stack[-1]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(p)
        
        if stack:
            return False
        else:
            return True


            