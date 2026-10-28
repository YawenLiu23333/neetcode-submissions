class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]

        for i in range(len(prefix)):
            for s in strs[1:]:
                if len(s) == 0:
                    return ""
                if i == len(s) or prefix[i] != s[i]:
                    return prefix[:i]
        return prefix

            

            

            

        
        