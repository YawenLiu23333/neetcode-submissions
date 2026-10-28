class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        for num, freq in Counter(nums).items():
            heap.append((freq, num))
        heapq.heapify(heap)
        while len(heap) > k:
            heapq.heappop(heap)

        return [item[1] for item in heap]
