class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        maxheap = []

        if a:
            heapq.heappush(maxheap, [-a, 'a'])
        if b:
            heapq.heappush(maxheap, [-b, 'b'])
        if c:
            heapq.heappush(maxheap, [-c, 'c'])
        
        output = []
        while maxheap:
            count, letter = heapq.heappop(maxheap)
            if len(output) >= 2 and output[-2] == output[-1] == letter:
                if not maxheap:
                    break

                count2, letter2 = heapq.heappop(maxheap)
                output.append(letter2)
                count2 += 1
                if count2 != 0:
                    heapq.heappush(maxheap, [count2, letter2])
                heapq.heappush(maxheap, [count, letter])
            else:
                output.append(letter)
                count += 1
                if count != 0:
                    heapq.heappush(maxheap, [count, letter])
             
        return ''.join(output)

                
            