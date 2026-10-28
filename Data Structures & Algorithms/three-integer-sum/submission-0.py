class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
       

        for i in range(0, len(nums)-1):

            l, r = i + 1, len(nums) - 1
   
            target = - nums[i]
            while l < r:
                if nums[l] + nums[r] == target:
                    res.add((nums[i], nums[l], nums[r]))
                    r -= 1
                    l += 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    l += 1
        return [list(r) for r in res]

