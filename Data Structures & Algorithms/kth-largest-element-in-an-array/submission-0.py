class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #edge case
        
        #heapify helper  
        def sift_down(c1: int, p: int, length: int) -> None:
            while c1 < length:
                big = c1
                c2 = c1 + 1
                if c2 < length and nums[c1] < nums[c2]:
                    big = c2
                
                if nums[p] < nums[big]:
                    nums[p], nums[big] = nums[big], nums[p]
                    p = big
                    c1 = p * 2 + 1
                else:
                    break
        
        check = (len(nums) - 2) // 2
        while check >= 0:
            p = check
            c1 = p * 2 + 1
            sift_down(c1, p, len(nums))
            check -= 1
        print(nums)
        #heappop
        end = len(nums) - 1
        while k > 0:
            nums[0], nums[end] = nums[end], nums[0]
            k -= 1
            end -= 1
            sift_down(1, 0, end + 1)
            print(k, end, nums[end])
        return nums[end + 1]
            


            