class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            if target - nums[i] in seen:
                j = target - nums[i]
               
                return [seen[j], i]
                
            
            seen[nums[i]] = i
            
                
        



            
