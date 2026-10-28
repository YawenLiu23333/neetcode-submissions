class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        res = 0
        stack = []
        for i in range(len(position)):
            stack.append([position[i], speed[i]])
        stack.sort(key = lambda x:x[0])

        while stack:
            time = (target - stack[-1][0]) / stack[-1][1] 
            stack.pop()
            while stack and time >= (target - stack[-1][0]) / stack[-1][1]:
                stack.pop()
            res += 1
        
        return res 
        


