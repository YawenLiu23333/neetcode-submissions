class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0]* 3
        for n in nums:
            count[n] += 1
   

        cur = 0
        for i in range(len(count)):
            while count[i] > 0 and cur < len(nums):
                nums[cur] = i
                count[i] -= 1
                cur += 1



        
