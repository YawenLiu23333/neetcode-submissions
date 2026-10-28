class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) -1
        while l <= r:
            m = (l + r) //2
            if target == nums[m]:
                return m 
            
            if nums[m] < nums[r]:
                if nums[m] < target <= nums[r]:
                    l += 1
                else:
                    r -= 1
            else:
                if nums[l] <= target < nums[m]:
                    r -= 1
                else:
                    l += 1

        return -1