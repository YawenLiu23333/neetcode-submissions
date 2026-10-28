class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = [0] * 26

        for n in s:
            count[ord(n)- ord('a')] += 1
        for n in t:
            if count[ord(n) - ord('a')] == 0:
                return False
            count[ord(n) - ord('a')] -= 1

        for i in range(len(count)):
            if count[i] != 0:
                return False
        return True
        