class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        minLen = min(len(word1), len(word2))
        result = ''
        for i in range(minLen):
            result += word1[i]
            result += word2[i]
        
        if len(word1) > minLen:
            result += word1[i+ 1:]

        if len(word2) > minLen:
            result += word2[i + 1:]

        return result

        