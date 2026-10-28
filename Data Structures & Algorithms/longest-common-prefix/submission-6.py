class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minlen = float('inf')

        for s in strs:
            if len(s) < minlen:
                minlen = len(s)
        i = 0
        while i < minlen:
            for s in strs:
                if s[i] != strs[0][i]:
                    return s[:i]
            i += 1
        
        return s[:i]                





            

            

            

        
        