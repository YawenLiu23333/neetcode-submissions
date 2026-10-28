class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums2 = []
        for n in nums:
            nums2.append(n)
        ans = nums + nums2
        return ans
        