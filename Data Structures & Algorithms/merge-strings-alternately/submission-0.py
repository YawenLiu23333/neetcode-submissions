class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        minlen = min(len(word1), len(word2))

        res =''
        for i in range(minlen):
            res += word1[i]
            res += word2[i]

        if len(word1) > minlen:
            for s in word1[i+1:]:
                res += s

        if len(word2) > minlen:
            for s in word2[i+1:]:
                res += s        
        
        return res