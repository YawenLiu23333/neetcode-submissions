class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash1= defaultdict(int)
        hash2 = defaultdict(int)
        for c in s:
            hash1[c]+=1
        for ct in t:
            hash2[ct]+=1
        
        return hash1 == hash2



        