class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l, r = 0, len(nums) - 1
        while l < len(nums):
            while l <= r and nums[l] == val:
                nums[l], nums[r] = nums[r], nums[l]
                r -= 1
            l += 1
        return r + 1
            
# 4,1,2,3,1
# i.    r
# 4,3,2,1,1 
#   i.r  

        