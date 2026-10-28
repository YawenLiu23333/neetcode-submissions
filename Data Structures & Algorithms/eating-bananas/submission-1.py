class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        l, r = 1, max(piles)
        res = max(piles)
        while l <= r:
            t = 0
            mid = (l + r) // 2
            for p in piles:
                t += math.ceil(p/mid)
            
            if t > h:
                l = mid + 1
            else:
                res = min(res, mid)
                r = mid - 1

        return res

             
            




