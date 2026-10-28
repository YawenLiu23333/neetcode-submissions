class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = {}
        for i in range(len(nums)):
            if nums[i] in count.values():
                return True
            # count[nums[i]] = nums[i]
            count[i] = nums[i]
            print(count)
        return False
