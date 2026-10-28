class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        l, r = max(weights), sum(weights)
        res = r

        def canShip(cap):
            ship = 1
            newCap = cap
            for w in weights:
                if cap - w < 0:
                    ship += 1
                    cap = newCap
                cap -= w
            return ship <= days

        while l <= r:
            mid = l + (r - l) //2
               
            if canShip(mid):
                res = min(res, mid)
                r = mid - 1
            else:
                l = mid + 1
        return res

          






