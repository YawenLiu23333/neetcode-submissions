class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        m = None
        count = 0
        for n in nums:
            if count == 0:
                m = n
            
            if n != m:
                count -= 1

            else:
                count += 1

        return m 

