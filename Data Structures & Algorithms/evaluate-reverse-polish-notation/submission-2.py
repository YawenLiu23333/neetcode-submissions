class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t == '+':
                new = stack[-1] + stack[-2]
                stack.pop()
                stack.pop()
                stack.append(new)
            elif t == '-':
                new = stack[-2] - stack[-1]
                stack.pop()
                stack.pop()
                stack.append(new)
            elif t == '*':
                new = stack[-1] * stack[-2]
                stack.pop()
                stack.pop()
                stack.append(new)
            elif t == '/':
                new = int(stack[-2]/ stack[-1])
                stack.pop()
                stack.pop()
                stack.append(new)
            else:
                stack.append(int(t))

        return stack[-1]
        