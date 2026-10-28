class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        stops = [0] * 1001
        for i in range(len(trips)):
            stops[trips[i][1]] += trips[i][0]
            stops[trips[i][2]] -= trips[i][0]

        total = 0
        for i in range(len(stops)):
            if stops[i] != 0:
                total += stops[i]
                if total > capacity:
                    return False
        return True
        