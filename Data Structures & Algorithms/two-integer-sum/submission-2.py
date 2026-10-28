class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            if target - nums[i] in seen:
                j = target - nums[i]
                print(i)
                print(seen[j])
                if i >= seen[j]:
                    return [seen[j], i]
                else:
                    return [i, seen[j]]
            
            seen[nums[i]] = i
            
                
        



            
