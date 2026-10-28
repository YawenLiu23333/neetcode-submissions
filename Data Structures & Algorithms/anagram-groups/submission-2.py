class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)
        #group strings by letters
        for s in strs:
            count = [0] *28
            for t in s:
                count[ord(t) - ord("a")] += 1
            group[tuple(count)].append(s)

        output = []
        for i, s in group.items():
            output.append(s)

        return output


        