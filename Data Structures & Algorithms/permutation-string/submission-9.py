class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        length = len(s1)
        count = Counter(s1)
        window = Counter(s2[:length])
        if count == window:
            return True
        
        l = 0
        for r in range(length, len(s2)):
            window[s2[r]] += 1
            window[s2[l]] -= 1
            if window[s2[l]] == 0:
                del window[s2[l]]
            l += 1
            if window == count:
                return True
        return False 
        

        