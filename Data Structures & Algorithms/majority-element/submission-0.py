class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        seen = defaultdict(int)
        for i in range(len(nums)):
            seen[nums[i]] += 1
        res = max(seen, key=seen.get)
        return res

        