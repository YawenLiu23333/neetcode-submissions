class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #o(1)space, o(n)run time
        count = 0
        temp = None
        for num in nums:
            if count == 0:
                temp = num

            if temp == num:
                count += 1
            else:
                count -= 1
        return temp

        

        

        




        
        



        

        