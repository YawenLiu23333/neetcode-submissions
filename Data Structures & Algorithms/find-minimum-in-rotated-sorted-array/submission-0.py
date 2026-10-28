class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = max(nums)
        while l <= r:
            mid = (r + l) // 2
            print(nums[mid])
            if nums[l] <= nums[mid] <= nums[r]:
                res = min(nums[l], res)
                return res
            elif nums[l] > nums[mid]:
       
                res = min(nums[mid], res)
       
                r = mid - 1
            elif nums[mid] > nums[r]:
                res = min(nums[r], res)
                l = mid + 1
        return res


