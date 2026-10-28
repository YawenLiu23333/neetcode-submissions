class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        count1 = defaultdict(int)
        count2 = defaultdict(int)

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            count1[s[i]] += 1
            count2[t[i]] += 1

        print(count1)
        print(count2)
        return count1 == count2


        


