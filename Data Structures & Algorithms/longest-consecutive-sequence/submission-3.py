class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        check = set(nums)
        longest = 0
        for i in range(len(nums)):
            if nums[i] - 1 not in check:
                length = 1
                increase = 1
                while nums[i] + increase in check:
                    length += 1
                    increase += 1
                longest = max(length, longest)
        return longest
        