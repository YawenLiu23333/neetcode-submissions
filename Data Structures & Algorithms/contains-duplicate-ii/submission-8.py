class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l = 0
        r = 1
        while r < len(nums):
            if nums[l] != nums[r]:
                r += 1
                if r - l > k:
                    l += 1
                    r = l + 1
            else:
                return True
        return False