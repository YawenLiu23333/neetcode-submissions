class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def mergesort(arr):            
            if len(arr) <= 1:
                return arr
            
            l, r = 0, len(arr) 
            mid = (r - l) // 2 

            left = mergesort(arr[l:mid])
            right = mergesort(arr[mid:r])

            return merge(left, right)

        def merge(left, right):
            res = []

            
            l = r = 0
            while l < len(left) and r < len(right): 
                if left[l] <= right[r]:
                    res.append(left[l])
                    l += 1
                else:
                    res.append(right[r]) 
                    r += 1

            if l < len(left):       
                res += left[l:]
            if r < len(right):
                res += right[r:]
   
            return res
        return mergesort(nums)


        
        









