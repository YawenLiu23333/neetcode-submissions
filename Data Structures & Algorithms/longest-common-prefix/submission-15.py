class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        length = float('inf')
        for s in strs:
            if len(s) < length:
                length = len(s)
        print(length)

        for l in range(length):
            for i in range(len(strs)):
                if strs[i][l] != strs[0][l]:
                    return strs[i][:l]
        if length > 0:
            return strs[0][:length]
        elif length == 0:
            return '' 
        else:
            return strs[0]
        


        