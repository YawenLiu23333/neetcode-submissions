class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = set()
        for i in range(len(nums)):
            if len(seen) > k:
                seen.remove(nums[i - k -1])
                print(i - k)
            if nums[i] in seen:
                print(seen)
                return True
            seen.add(nums[i])
        return False
            