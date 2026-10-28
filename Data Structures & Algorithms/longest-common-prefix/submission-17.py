class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        length = float('inf')
        for s in strs:
            length = min(len(s), length)

        prefix = strs[0][:length]
        for l in range(length):
            for i in range(len(strs)):
                if strs[i][l] != prefix[l]:
                    return prefix[:l]
        
        return prefix


