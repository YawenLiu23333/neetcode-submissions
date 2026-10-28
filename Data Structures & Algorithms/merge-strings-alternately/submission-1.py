class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        minlen = min(len(word1), len(word2))
        new = ''

        for i in range(minlen):
            new += word1[i]
            new += word2[i]
        
        if len(word1) > i:
            new += word1[i + 1:]

        if len(word2) > i:
            new += word2[i + 1:]

        return new