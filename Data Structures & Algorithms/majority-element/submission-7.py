class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = defaultdict(int)
        for n in nums:
            count[n] += 1
        
        res = 0
        ans = None
        for k, v in count.items():
            if v > res:
                res = v
                ans = k

        return ans


        


        

        

        

        




        
        



        

        