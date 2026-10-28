class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        check = set(nums)
        longest = 0
        for n in nums:
 
            if n-1 not in check:
                long = 1
                while n + long in check:
                    long += 1
                longest = max(longest, long)

        return longest


        