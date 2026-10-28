class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        count = []
        if a != 0:
            heapq.heappush(count, [-a,'a'])
        if b != 0:
            heapq.heappush(count, [-b,'b'])
        if c != 0:
            heapq.heappush(count, [-c,'c'])
        print(count)
        
        res = []
        while count:
            temp = heapq.heappop(count)
            print(count)
            if len(res) >= 2 and res[-1] == res[-2] == temp[1]:
                if not count:
                    break
                temp2 = heapq.heappop(count)
                res.append(temp2[1])
                temp2[0] += 1
                if temp2[0] != 0:
                    heapq.heappush(count, temp2)
            
            res.append(temp[1])
            temp[0] += 1

            if temp[0] != 0:
                heapq.heappush(count, temp)

        return ''.join(res)      


        