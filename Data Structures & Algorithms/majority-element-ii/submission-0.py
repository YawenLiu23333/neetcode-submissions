class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        #edge case
        if len(nums) <= 2:
            return nums
        nums.sort()
        res = set()
        l, r = 0, 1
    #add each number to res when they appear more than n/3
        while r < len(nums):
            if nums[l] == nums[r]:
                print(nums[l])
                if nums[l] not in res and r - l + 1 > len(nums)/3:
                    res.add(nums[l])
                    print(res)
            else:
                l = r
            r += 1    
        return list(res)
                
            



        


        