class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hasmap = {}
        for i in range(len(nums)):
            res = target - nums[i]
            if res in hasmap:
                return sorted([i, hasmap[res]])
            hasmap[nums[i]] = i
            
                
        



            
