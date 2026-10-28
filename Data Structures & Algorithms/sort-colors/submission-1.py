class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0] * 3
        for n in nums:
            count[n] += 1
        
        j = 0
        for i in range(len(nums)):
            while count[j] == 0:
                j += 1
            count[j] -= 1   
            nums[i] = j
            
                   

#0,2,1   0
#0,1,1.  0,1
#0,0,1.  0,1,1
#0,0,0.  0,1,1,2