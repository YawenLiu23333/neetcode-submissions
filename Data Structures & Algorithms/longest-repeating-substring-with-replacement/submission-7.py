class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        check = defaultdict(int)
        l = 0
        longest = 0
        freq = 0
        for r in range(len(s)):
            check[s[r]] += 1
            # print('1', check)
            freq = max(freq, check[s[r]])
            while r - l + 1 - freq > k:
                # print(check)
                check[s[l]] -= 1
                l += 1
                
                # print('2', check)
            # print('0', r - l + 1, check)
            longest = max(r - l + 1, longest)
        return longest