class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                new1 = s[l:r]
                new2 = s[l+1:r+1]
                return new1 == new1[::-1] or new2 == new2[::-1]
        return True
        

        

        