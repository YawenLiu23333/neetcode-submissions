class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for i in range(len(prefix)):
            for j in range(len(strs)):
                if i >= len(strs[j]) or strs[j][i] != prefix[i]:
                    return prefix[:i]
        return prefix
        