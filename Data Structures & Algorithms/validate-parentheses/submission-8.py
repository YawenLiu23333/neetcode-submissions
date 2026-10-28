class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False
        stack = []
        check = {'{':'}', '[':']', '(':')'}
        for c in s[::-1]:
            if c in check.values():
                stack.append(c)
                print(1)
            else:
                if not stack or stack[-1] != check[c]:
                    print(2)
                    return False
                stack.pop()
        if stack:
            print(3)
            return False
        return True



        