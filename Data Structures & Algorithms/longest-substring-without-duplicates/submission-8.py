class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = []
        l = 0
        long = 0
        for i in range(len(s)):
            while s[i] in seen:
                seen.remove(s[l])
                l += 1

            seen.append(s[i])
            count = len(seen)
            long = max(count, long)

        return long
                


        
                

            

        