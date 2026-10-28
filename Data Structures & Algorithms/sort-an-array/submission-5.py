class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        #heapify nums
        n = len(nums)
        if n == 1:
            return nums
        i = (n - 2) // 2
        while i >= 0:
            C1 = i * 2 + 1
            C2 = i * 2 + 2
            big = C1
            if C2< len(nums) and nums[C1] < nums[C2]:
                big = C2
            if nums[i] < nums[big]:
                nums[i], nums[big] = nums[big], nums[i]
                p = big
                c1 = p * 2 + 1
                while c1 < n:
                    bigger = c1
                    c2 = p * 2 + 2
                    if c2< len(nums) and nums[c1] < nums[c2]:
                        bigger = c2 
                    if nums[p] < nums[bigger]:
                        nums[p], nums[bigger] = nums[bigger], nums[p]
                        p = bigger
                        c1 = p * 2 + 1
                    else:
                        break
            i -= 1                
        #5,2,3,1

        #delete numbers form the heap
        end = len(nums) - 1
        while end > 0:
            nums[0], nums[end] = nums[end], nums[0]
            end -= 1

            #pick bigger child
            p = 0
            c1 = p * 2 + 1
            while c1 <= end: 
                big =c1
                c2 = p * 2 + 2
                if  c2 <= end and nums[c1] < nums[c2]:
                    big = c2
                if nums[p] < nums[big]:
                    nums[p], nums[big] = nums[big], nums[p]
                    p = big
                    c1 = p * 2 + 1
                else:
                    break
        return nums                
        #1,2,3,5
        #3,2,1,5
        #1,2,3,5
        #2,1,3,5
        #1,2,3,5


            

        







            

        