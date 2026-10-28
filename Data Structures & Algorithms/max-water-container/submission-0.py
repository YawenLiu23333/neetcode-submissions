class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0 , len(heights) - 1

        maxWater = 0
        while l < r:
            water = min(heights[l],heights[r]) * (r - l)
            if heights[l] > heights[r] and l < r:
                r -= 1
            elif heights[l] < heights[r] and l < r:
                l += 1
            else:
                l += 1
            maxWater = max(water, maxWater)

        return maxWater