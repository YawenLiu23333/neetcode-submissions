class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res = []
        heap = []
        if a > 0:
            heapq.heappush(heap,[-a,'a'])
        if b > 0:
            heapq.heappush(heap,[-b,'b'])
        if c > 0:
            heapq.heappush(heap, [-c,'c'])
        
        while heap:
            temp = heapq.heappop(heap)

            if temp[0] == 0:
                break
            if len(res) >= 2 and res[-1] == temp[1] and res[-2] == temp[1]:

                if not heap:
                    return res
                nxt = heapq.heappop(heap)
                if nxt[0] != 0:
                    res.append(nxt[1])

                    nxt[0] += 1
                    heapq.heappush(heap, temp)
                    heapq.heappush(heap, nxt)
            else:
                res.append(temp[1])
                temp[0] += 1
                heapq.heappush(heap, temp)
        return ''.join(res)

            




        