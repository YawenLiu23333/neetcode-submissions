class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = [0] * 26
        res = []
        for c in s:
            freq[ord(c) - ord('a')] += 1
            if freq[ord(c) - ord('a')] > (len(s) + 1) / 2:
                return ''
        maxIdx = freq.index(max(freq))
        
        
        while len(res) < len(s):
            maxIdx = freq.index(max(freq))
            res.append(chr(maxIdx + ord('a')))
            freq[maxIdx] -= 1
            if freq[maxIdx] == 0:
                continue
            
            temp = freq[maxIdx]
            freq[maxIdx] = float('-inf')
            nxtmaxIdx = freq.index(max(freq))
            res.append(chr(nxtmaxIdx + ord('a')))
            freq[nxtmaxIdx] -= 1
            freq[maxIdx] = temp

        return ''.join(res)

