class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = set()
        l = r = 0
        while r < len(nums):
            seen.add(nums[l])
            l += 1
            while r < len(nums) and nums[r] in seen:
                r += 1
            if l < len(nums) and r < len(nums):
                nums[l], nums[r] = nums[r], nums[l]
        return l
        

        


        