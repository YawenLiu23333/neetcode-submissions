class Solution:
    def validPalindrome(self, s: str) -> bool:

        def isPali(strs):
            return strs == strs[::-1]

        l = 0
        r = len(s) -1
        while l < r:
 
            if s[l] != s[r]:
                return isPali(s[l:r]) or isPali(s[l+1:r+1])
                
            l += 1
            r -= 1
        return True

        