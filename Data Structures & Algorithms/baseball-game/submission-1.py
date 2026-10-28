class Solution:
    def calPoints(self, operations: List[str]) -> int:
        seen = []
        for o in operations:
            if o == '+':
                seen.append(seen[-1] + seen[-2])
            elif o == 'C':
                seen.pop()
            elif o == 'D':
                seen.append(seen[-1] * 2)
            else:
                seen.append(int(o))

        res = 0    
        while seen:
            res += seen.pop()

        return res





           
                