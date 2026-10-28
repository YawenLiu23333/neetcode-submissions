class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        for i, n in enumerate(nums):
            l, r = i + 1, len(nums) - 1
            target = 0 - n
            while l < r:
                if nums[l] + nums[r] == target:
                    res.add(tuple([n, nums[l], nums[r]]))
                    l += 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    l += 1
        return list(res)



            
