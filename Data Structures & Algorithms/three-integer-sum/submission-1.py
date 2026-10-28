class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        seen = set()
        for i in range(len(nums) - 1):
            target = 0 - nums[i]
            l , r = i + 1, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] > target:
                    r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    seen.add(tuple([nums[i], nums[l], nums[r]]))
                    r -= 1
        return list(seen)

