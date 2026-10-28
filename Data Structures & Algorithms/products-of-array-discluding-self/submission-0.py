class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre = [0] * n
        after = [0] * n
        res = [0] * n
        
        pre[0] = after[n - 1] = 1

        p = nums[0]
        for i in range(1, len(nums)):
            print(p)
            pre[i] = p
            p *= nums[i]
            
        print(pre)

        p = nums[n - 1]
        for i in range(len(nums)-2, -1, -1):
            after[i] =  p
            p *= nums[i]
        print(after)

        for i in range(len(nums)):
            res[i] = pre[i] * after[i]

        return res

            