class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #O(1)space solution
        
        seen = set(nums)
        occur = res = []
        for m in seen:
            l = count = 0
            while l < len(nums):
                if nums[l] == m:
                    count += 1
                l += 1
                occur = [count, m]
            res = max(occur, res)
        return res[1]
        



        

        