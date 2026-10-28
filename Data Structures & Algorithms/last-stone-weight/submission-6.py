class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones:
            heapq.heappush(heap, -stone)

        while len(heap) >= 2:
            x = heapq.heappop(heap)
            y = heapq.heappop(heap)
            remain = abs(x - y)
            if remain != 0:
                heapq.heappush(heap, -remain)
        
        return -heap[0] if heap else 0