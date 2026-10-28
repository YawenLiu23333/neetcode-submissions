class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profit = 0
        each = 0
        small = prices[0]

        for i in range(len(prices)):

            if prices[i] < small:            
                small = prices[i]
            if prices[i] > small:
                each = prices[i] - small

            profit = max(each, profit)
        
        return profit               