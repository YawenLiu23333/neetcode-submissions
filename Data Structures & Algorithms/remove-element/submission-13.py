class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        cur = 0
        r = len(nums) - 1
        while cur <= r:
            if nums[cur] == val:
                nums[cur], nums[r] = nums[r], nums[cur]
                r -= 1
            else:
                cur += 1
        return r + 1


        