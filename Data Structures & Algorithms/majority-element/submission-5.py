class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #o(n)space, o(n)run time
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        
        ans = -1
        c = 0
        for key,val in count.items():

            if val > c:
                ans = key
                c = val
        return ans

        

        




        
        



        

        