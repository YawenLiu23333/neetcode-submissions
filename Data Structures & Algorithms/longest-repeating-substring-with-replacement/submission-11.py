class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        res = 0
        seen = defaultdict(int)
        for r in range(len(s)):
            seen[s[r]] += 1
            while r - l + 1 - max(seen.values()) > k:
                seen[s[l]] -= 1
                if seen[s[l]] == 0:
                    del seen[s[l]]
                l += 1
            res = max(res, r - l + 1)
        return res
            
