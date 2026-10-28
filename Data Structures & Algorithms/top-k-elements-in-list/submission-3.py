class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = defaultdict(int)
        for n in nums:
            res[n] += 1
        

        out = [[] for i in range(len(nums) + 1)]
        for n, freq in res.items():
            out[freq].append(n)
   
        
        output = []
        for i in range(len(out)-1, 0, -1):
            for n in out[i]:
                output.append(n)
                if len(output) == k:
                    return output
        
            
            