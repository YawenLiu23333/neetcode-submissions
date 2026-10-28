class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        #create dic for count
        cnt = Counter(hand)
        heap = list(cnt.keys())
        heapq.heapify(heap)

        #create min heap to keep track of smallest number
        while heap:
            start = heap[0]
            for x in range(start, start + groupSize):
                if cnt[x] == 0:
                    return False
                cnt[x] -= 1
                if cnt[x] == 0:
                    if x != heap[0]:
                        return False
                    heapq.heappop(heap)
        return True
                


