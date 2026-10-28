class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)

        longest = 0
        for n in nums:
            if (n - 1) not in seen:
                seq = 1
                num = n
                while (num + 1) in seen:
                    seq += 1
                    num += 1
                longest = max(seq, longest)

        return longest


                

