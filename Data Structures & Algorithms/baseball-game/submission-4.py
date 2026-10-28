class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        total = 0
        for op in operations:
            if op == '+':
                add = stack[-1] + stack[-2]
                stack.append(add)
                # print('2 int are: ',temp, temp2, 'stack after appending is: ', stack)
                total += add
            elif op == 'D':
                # print(temp)
                double = stack[-1] * 2
                stack.append(double)
                # print(stack)
                total += double
            elif op == 'C':
                temp = stack.pop()
                total -= temp
            else:
                stack.append(int(op))
                # print('int is :', op, 'stack after append int is: ', stack)
                total += int(op)
        # print('final stack looks like: ', stack)
        return total
        