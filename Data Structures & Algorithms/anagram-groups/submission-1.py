class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        
        for word in strs:
            count = [0]*26
   
            for letter in word:
                count[ord(letter) - ord("a")] += 1
            if tuple(count) in res:
                res[tuple(count)].append(word)
            else:
                res[tuple(count)] = [word]
        print(res)
        out = []
        for k, v in res.items():
            out.append(v)
        return out

        