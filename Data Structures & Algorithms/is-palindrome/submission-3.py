class Solution:
    def isPalindrome(self, s: str) -> bool:

        def isAlphan(c):
            if ord('a')<= ord(c) <= ord('z') or ord('A')<= ord(c) <= ord('Z') or ord('0')<= ord(c) <= ord('9'):
                return True
        
        l = 0
        r = len(s) - 1
        while l < r:
            print("loop", l, s[l], s[r])
            if isAlphan(s[l]) and isAlphan(s[r]):
                if s[l].lower() != s[r].lower():
                    return False
                l += 1
                r -= 1
            
            if not isAlphan(s[l]):
                l += 1
            
            if not isAlphan(s[r]):
                r -= 1

        return True
