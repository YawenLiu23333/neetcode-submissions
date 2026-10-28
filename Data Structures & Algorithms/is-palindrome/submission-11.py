class Solution:
    def isPalindrome(self, s: str) -> bool:

        def isAlnum(char):
            return (ord('a') <= ord(char) <= ord('z') 
            or ord('A') <= ord(char) <= ord('Z') 
            or ord('0') <= ord(char) <= ord('9'))
        
        l, r = 0, len(s) - 1
        while l < r:
            if not isAlnum(s[l]):
                l += 1
            elif not isAlnum(s[r]):
                r -= 1
            else:
                if s[l].lower() == s[r].lower():
                    l += 1
                    r -= 1
                elif s[l].lower() != s[r].lower():
           
                    return False
        return True
            
        