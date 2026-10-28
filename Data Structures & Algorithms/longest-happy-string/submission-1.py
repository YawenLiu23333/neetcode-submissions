class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res = ''
        heap = []
        heapq.heappush(heap,[-a,'a'])
        heapq.heappush(heap,[-b,'b'])
        heapq.heappush(heap, [-c,'c'])
        
        nxt = None
        while heap:
            temp = heapq.heappop(heap)

            if temp[0] == 0:
                break
            if len(res) >= 2 and res[-1] == temp[1] and res[-2] == temp[1]:
                print('temp occurs 2 times')
                if not heap:
                    return res
                nxt = heapq.heappop(heap)
                if nxt[0] != 0:
                    res += nxt[1]
                    print('res is', res)
                    nxt[0] += 1
                    heapq.heappush(heap, temp)
                    heapq.heappush(heap, nxt)
            else:
                res += temp[1]
                temp[0] += 1
                heapq.heappush(heap, temp)
        return res

            




        