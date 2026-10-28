class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # heapq.heapify(nums)
        # return nums[k]
        heap = []
        for n in nums:
            heapq.heappush(heap, -n)
        while k > 0:
            res = heapq.heappop(heap)
            k -= 1
        return -res