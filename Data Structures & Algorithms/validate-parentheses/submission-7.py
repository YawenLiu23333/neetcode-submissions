class Solution:
    def isValid(self, s: str) -> bool:
        check = {')': '(', '}': "{", ']': '['}
        stack = []
        for b in s:
            if b not in check:
                stack.append(b)
            else:
                if not stack:
                    return False
                temp = stack.pop()
                # print(check[b], temp)
                if check[b] != temp:
                    # print('1')
                    return False
        if len(stack) == 0:
            return True
        else:
            return False