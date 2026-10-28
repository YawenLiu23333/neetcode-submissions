class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = [(freq, n) for n, freq in Counter(nums).items()]
        heapq.heapify(heap)
        while len(heap) > k:
            heapq.heappop(heap)
        return [n[1] for n in heap]