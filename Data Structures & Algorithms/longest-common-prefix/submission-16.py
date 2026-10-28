class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        length = float('inf')
        for s in strs:
            if len(s) < length:
                length = len(s)
    

        for l in range(length):
            for s in strs:
                if s[l] != strs[0][l]:
                    return strs[0][:l]
        return strs[0][:length]
        

        


        