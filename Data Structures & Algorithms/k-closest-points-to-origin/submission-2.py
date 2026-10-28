class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = [] 
        for i in range(len(points)):
            heapq.heappush(heap, [math.sqrt(pow(points[i][0], 2) + pow(points[i][1],2)), points[i]])
        print(heap)

        res = []
        while k > 0:
            temp = heapq.heappop(heap)
            res.append(temp[1])
            k -= 1
        
        return res

        