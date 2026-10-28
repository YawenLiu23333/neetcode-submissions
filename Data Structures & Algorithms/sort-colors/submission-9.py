class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r = 0, len(nums) - 1
        i = 0
        while i < len(nums):
            # print('loop ',i, 'nums[i] is', nums[i])
            if nums[i] == 0:
                # print('l is: ', l, 'nums[l] is', nums[l])
                nums[l], nums[i] = nums[i], nums[l]
                # print('nums is ', nums)
                l += 1
                i += 1
            elif nums[i] == 2 and i <= r:
                # print('r is: ', r, 'nums[r] is', nums[r])
                nums[i], nums[r] = nums[r], nums[i]
                # print('nums is ', nums)
                r -= 1
            else:
                i += 1
        # 2,1,0
        # 2,0,1
        # 1,0,2
        # 0,1,2

