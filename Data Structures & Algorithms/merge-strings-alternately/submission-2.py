class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        minlen = min(len(word1), len(word2))
        new = ''
        for i in range(minlen):
            new += word1[i]
            new += word2[i]
        
        i += 1
        while i <= len(word1) -1:
            new += word1[i]
            i += 1
        
        while i <= len(word2) -1:
            new += word2[i]
            i += 1
        
        return new