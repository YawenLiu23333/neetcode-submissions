class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = Counter(s1)
        count2 = defaultdict(int)

        if len(s1) > len(s2):
            return False
        
        l = 0
        for i in range(len(s2)):
            # print(i, s2[i], count2, count)
            
            count2[s2[i]] += 1
            if i > len(s1) - 1:
                count2[s2[l]] -= 1
                if count2[s2[l]] == 0:
                    del count2[s2[l]]
                l += 1
            if count == count2:
                return True

        return False
            

            

