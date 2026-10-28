class Solution:
    def reorganizeString(self, s: str) -> str:
        count = defaultdict(int)
        for c in s:
            count[c] += 1
        
        maxVal = max(count.values())
        if  maxVal > (len(s) + 1) //2 :
            return ""

        sort = []
        for c, cnt in count.items():
            heapq.heappush(sort, [-cnt, c])

        res = []
        while sort:
            temp = heapq.heappop(sort)
            if len(res) >=1 and res[-1] == temp[1]:

                temp2 = heapq.heappop(sort)
                if not temp2:
                    break
                res.append(temp2[1])
                temp2[0] += 1

                if temp2[0]!= 0:
                    heapq.heappush(sort,temp2)

            res.append(temp[1])
            temp[0] += 1
            if temp[0] != 0:
                heapq.heappush(sort, temp)
        
        if len(res) == len(s):
            return ''.join(res)
        else:
            return ''



        