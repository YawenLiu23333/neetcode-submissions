class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        count1, count2 = defaultdict(int), defaultdict(int)
        for i in range(len(s1)):
            count1[s1[i]] += 1
            count2[s2[i]] += 1
        
        if count1 == count2:
            return True

        for j in range(i + 1, len(s2)):
            count2[s2[j]] += 1
            count2[s2[j - len(s1)]] -= 1
            if count2[s2[j - len(s1)]] == 0:
                del count2[s2[j - len(s1)]]
            
            if count1 == count2:
                return True
                
        return False

