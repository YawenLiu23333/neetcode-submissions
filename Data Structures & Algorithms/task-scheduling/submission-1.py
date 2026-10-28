class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        avail = [[-freq, task] for task, freq in Counter(tasks).items()]
        heapq.heapify(avail)
        time = 0
        cool = deque()
        while avail or cool:
            if cool and cool[0][0] == time:
                avail_time, freq, task = cool.popleft()
                heapq.heappush(avail,[freq, task])
            if avail:
                freq, task = heapq.heappop(avail)
                freq += 1
                if freq != 0:
                    cool.append((time + n + 1, freq, task))
            time += 1
        return time

                
            