class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        res = max(piles)
        l, r = 1, max(piles)
        while l <= r:
            mid = l + (r - l) // 2
            time = 0
            for p in piles:
                if time > h:
                    break
                if math.ceil(p/mid) <= 1:
                    time += 1
                else:
                    time += int(math.ceil(p/mid))
            if time > h:
                l = mid + 1
            else:
                res = min(res, mid)
                r = mid - 1
        return res



