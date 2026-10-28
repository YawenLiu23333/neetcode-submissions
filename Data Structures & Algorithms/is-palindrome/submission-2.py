class Solution:
    def isPalindrome(self, s: str) -> bool:

        def isalphaNum(c):
            return (ord("A") <= ord(c) <= ord("Z") or
                    ord("a") <= ord(c) <= ord("z") or
                    ord("0") <= ord(c) <= ord("9") )

        new = ""
        for c in s:
            if isalphaNum(c):
                new += c.lower()

        return new == new[::-1]