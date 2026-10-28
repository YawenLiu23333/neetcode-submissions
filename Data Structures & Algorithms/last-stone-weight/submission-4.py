class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap = [-stone for stone in stones]
        heapq.heapify(maxheap)
        while len(maxheap) > 1:
            x = heapq.heappop(maxheap)
            y = heapq.heappop(maxheap)
            if x - y < 0:
                heapq.heappush(maxheap, x - y)
        if maxheap:
            last = heapq.heappop(maxheap)
            return -last
        else:
            return 0
        