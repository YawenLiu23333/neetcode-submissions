class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = defaultdict(list)
        for s in strs:
            count = Counter(s)
            after = tuple(sorted(count.items()))
            output[after].append(s)
        result = list(output.values())
        return result