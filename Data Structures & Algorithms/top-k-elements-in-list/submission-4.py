class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for i in range(len(nums)):
            count[nums[i]] += 1
        print(count)
        out = [[] for i in range(len(nums) + 1)]
        print(out)
        for i, n in count.items():
            out[n].append(i)

        res = []
        for i in range(len(out)-1, 0, -1):
            for n in out[i]:
                res.append(n)
                if len(res) == k:
                    return res
        
            
            