class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        
        for i, n in enumerate(nums):
            diff = target - n
            if diff in seen:
                return sorted([i, seen[diff]])
            seen[n] = i

