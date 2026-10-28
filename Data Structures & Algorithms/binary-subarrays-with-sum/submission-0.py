class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def atMost(goal):
            if goal < 0:
                return 0

            count = 0
            res = 0
            l = 0
            for r in range(len(nums)):
                res += nums[r]
                while res > goal:
                    res -= nums[l]
                    l += 1
                count += r - l + 1
            return count

        ans = atMost(goal) - atMost(goal - 1)
        return ans