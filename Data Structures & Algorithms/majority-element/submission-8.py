class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #O(1)space O(n)time
        count = 0
        ans = nums[0]
        for n in nums:
            if count == 0:
                ans = n
            if ans == n:
                count += 1
            elif ans != n:
                count -= 1
        
        return ans


        


        

        

        

        




        
        



        

        