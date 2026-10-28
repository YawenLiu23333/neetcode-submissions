class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        start = 0
        k = end = len(nums) - 1
        while start <= end:
            while nums[start] == val and start <= end:
                nums[start], nums[end] = nums[end], nums[start]
                end -= 1
            start += 1
        return end + 1
#1

        