class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        k = k % len(nums)
        
        l, r = 0, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r],nums[l]
            l += 1
            r -= 1

        l1, r1 = 0, k - 1
        while l1 < r1:
            nums[l1], nums[r1] = nums[r1],nums[l1]
            l1 += 1
            r1 -= 1

        l2, r2 = k, len(nums) - 1
        while l2 < r2:
            nums[l2], nums[r2] = nums[r2],nums[l2]
            l2 += 1
            r2 -= 1
        

        
