class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        length = float('inf')
        for s in strs:
            length = min(len(s), length)

        
        for i in range(length):
            for s in strs:
                if s[i] != strs[0][i]:
                    return strs[0][:i]
        return strs[0][:length]
 
            

            
            
        
                
                


        
          
            

        






            

            

            

        
        