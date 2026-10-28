class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = p = 0
        l, r = 0, 1
        while r < len(prices):
            if prices[l] < prices[r]:
                p = prices[r] - prices[l]
                r += 1
            else:
                l = r
                r += 1
            res = max(res, p)

        return res
        