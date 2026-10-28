class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = set()
        l = r = 0
        while r < len(nums):
            seen.add(nums[r])    
            r += 1
            while r - l > k:
                seen.remove(nums[l])
                l += 1
            if r < len(nums) and nums[r] in seen:
                return True
        return False
            
            


        
        

        

        