class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hash1, hash2 = defaultdict(int), defaultdict(int)
        for n in s:
            hash1[n] = hash1.get(n, 0) + 1
        for n in t:
            hash2[n] = hash2.get(n, 0) + 1

        return hash1 == hash2
        