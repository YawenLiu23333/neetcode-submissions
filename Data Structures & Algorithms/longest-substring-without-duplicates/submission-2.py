class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        seq = 0
        res = 0

        l, r = 0, 0
        while r < len(s):
            if s[r] not in seen:
                seen.add(s[r])
                seq += 1
                r += 1
            else:
                
                seen.remove(s[l])
                l += 1
                seq -= 1
            
            res = max(seq, res)
            print(seen)

        return res
            

        