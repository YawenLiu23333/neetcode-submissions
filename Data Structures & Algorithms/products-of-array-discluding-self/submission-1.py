class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)

        cur = nums[0]
        for i in range(1, len(nums)):
            output[i] = cur
            cur *= nums[i]
        print('after pre operation, output is', output)
        # print(post)
        cur = nums[-1]
        for i in range(len(nums)-2, -1, -1):
            # print(i)
            output[i] *= cur
            cur *= nums[i]
        print('after post operation, output is', output)

        return output




        