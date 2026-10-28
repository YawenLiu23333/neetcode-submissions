class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for n in nums:
            count[n] += 1
        print(count)

        i = len(nums) + 1
        freq = [[] for _ in range (i)]


        for n, f in count.items():
    
            freq[f].append(n)


        res = []
        for i in range(len(freq) - 1, 0, -1):
            print("i is: ", i)
            for n in freq[i]:
                print("n is: ", n)
                res.append(n)
                k -= 1
                if k == 0:
                    return res



        
            
            