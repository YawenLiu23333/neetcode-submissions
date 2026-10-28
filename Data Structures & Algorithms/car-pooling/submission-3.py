class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        stops = [0] * 1001
        for p, start, to in trips:
            stops[start] += p
            stops[to] -= p

        total = 0
        for i in range(len(stops)):
            total += stops[i]
            if total > capacity:
                return False
        return True
        