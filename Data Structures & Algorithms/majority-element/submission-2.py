class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #O(1)space O(n)time 
        res = nums[0] 
        count = 0
        for n in nums:
            if res == n: 
                count += 1
            else:
                count -= 1
                if count == -1:
                    res = n
                    count = 1
        return res


        
        



        

        