class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        length = float('inf')
        for s in strs:
            length = min(len(s), length)

        prefix = strs[0][:length]
        for s in strs:
            for l in range(len(prefix)):
                if s[l] != prefix[l]:
                    prefix = s[:l]
                    break
        return prefix