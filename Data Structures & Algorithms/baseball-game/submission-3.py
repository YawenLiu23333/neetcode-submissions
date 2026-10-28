class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        total = 0
        for op in operations:
            if op == '+':
                temp = stack.pop()
                temp2 = stack.pop()
                add = temp + temp2
                stack.append(temp2)
                stack.append(temp)
                stack.append(add)
                # print('2 int are: ',temp, temp2, 'stack after appending is: ', stack)
                total += add
            elif op == 'D':
                temp = stack.pop()
                # print(temp)
                double = temp * 2
                stack.append(temp)
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
        