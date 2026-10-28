class Solution:
    def calPoints(self, operations: List[str]) -> int:
        see = []

        ans = 0
        for op in operations:
            if op == '+':
                new = see[-1] + see[-2]
                see.append(new)
            elif op == 'D':
                new = see[-1] * 2
                see.append(new)
            elif op == 'C':
                see.pop()
            else:
                new = int(op)
                see.append(new)

        while see:
            new = see.pop()
            ans += new

        return ans




           
                