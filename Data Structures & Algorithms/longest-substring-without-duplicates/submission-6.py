class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l = 0
        res = 0
        for i in range(len(s)):
        
            
            if s[i] in seen:
                while s[l] != s[i]:
                    seen.remove(s[l])
                    l += 1
                l += 1
            else:
                seen.add(s[i])
            res = max (len(seen), res)
 
        return res
                

            

        