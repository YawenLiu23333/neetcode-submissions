class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        calc = 0
        res = float('inf')
        l = 0
        for r in range(len(nums)):
            calc += nums[r]
            print(calc)
            while calc >= target:
                res = min(res, r - l + 1)
                print('res is', res)
                calc -= nums[l]
                l += 1

        if res != float('inf'):
            return res
        else:
            return 0
            
            
