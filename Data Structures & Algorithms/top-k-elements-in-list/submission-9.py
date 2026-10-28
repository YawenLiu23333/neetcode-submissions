class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        res = []
        for num, count in counts.items():
            heapq.heappush(res, [count, num])
            if len(res) > k:
                heapq.heappop(res)

        return [item[1] for item in res]