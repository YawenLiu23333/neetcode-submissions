class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        n = len(nums)
        while i < n:
            if nums[i] == val:
                nums[i], nums[n-1] = nums[n-1], nums[i]
                n -= 1
            else:
                i += 1
        return n

# 1, 2, 2, 3, 5
# i:0, n:5
# 1, 2, 2, 3, 5 i:1
# 1, 5, 2, 3, 2 n:4
# 1, 5, 2, 3, 2 i:2
# 1, 5, 3, 2, 2 n:3
# 1, 5, 3, 2, 2 i:3


