class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = []
        for i in range(len(nums)-1, -1, -1):

            if nums[i] in seen:
                del nums[i]
            else:
                seen.append(nums[i])
 

        k = len(seen)
        return k


        