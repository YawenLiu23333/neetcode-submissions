class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        res = 0
        stack = []
        for i in range(len(position)):
            stack.append([position[i], speed[i]])
        stack.sort(key = lambda x:x[0])
        print(stack)

        while stack:
            print(stack[-1])
            time = (target - stack[-1][0]) / stack[-1][1] 
            stack.pop()
            # print('top element after pop',stack[-1], 'time is', time, 'new time is',(target - stack[-1][0]) / stack[-1][1] )
            while stack and time >= (target - stack[-1][0]) / stack[-1][1]:
                # print('loop pop',stack[-1])
                stack.pop()

            res += 1
            # print('res after increment', res)
        return res 
        

        


