class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        check = Counter(s1)
        count = defaultdict(int)
        for i in range(len(s2)):
            count[s2[i]] += 1

            if i > len(s1) - 1:
                leftChar = s2[i - len(s1)]
                # print(leftChar)
                count[leftChar] -= 1
                if count[leftChar] == 0:
                    del count[leftChar]
            if count == check:
                return True
            

        return False

        