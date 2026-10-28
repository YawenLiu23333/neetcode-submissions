class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = [0] * 26
        count = []
        res = []
        for c in s:
            freq[ord(c) - ord('a')] += 1
            if freq[ord(c) - ord('a')] > (len(s) + 1) / 2:
                return ''
        
        for i, n in enumerate(freq):
            if n != 0:
                heapq.heappush(count,[-n, i])
        
        while len(res) < len(s):
            temp = heapq.heappop(count)
            res.append(chr(temp[1] + ord('a')))
            temp[0] += 1
            if temp[0] == 0:
                continue
            
            nxt = heapq.heappop(count)
            res.append(chr(nxt[1] + ord('a')))
            nxt[0] += 1

            if temp[0] != 0:
                heapq.heappush(count, temp)
            if nxt[0] != 0:
                heapq.heappush(count, nxt)
        
        return ''.join(res)


        
        
