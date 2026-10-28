class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergeSort(arr, l, r):
            if l == r:
                return 

            if l + 1 == r:
                if arr[l] >= arr[r]:
                    arr[l], arr[r] = arr[r], arr[l]
                return

            mid = (l + r) // 2

            mergeSort(arr, l, mid)
            mergeSort(arr, mid, r)

            left = arr[l:mid]
            right = arr[mid:r+1]
            leftIndex = 0
            rightIndex = 0

            for i in range(l, r + 1):
                if leftIndex < len(left) and rightIndex < len(right):
                    if left[leftIndex] <= right[rightIndex]:
                        arr[i] = left[leftIndex]
                        leftIndex += 1
                    else:
                        arr[i] = right[rightIndex]
                        rightIndex += 1
                elif leftIndex < len(left):
                    arr[i] = left[leftIndex]
                    leftIndex += 1
                elif rightIndex < len(right):
                    arr[i] = right[rightIndex]
                    rightIndex += 1

        mergeSort(nums, 0, len(nums)-1)
        return nums

        # def mergeSort(arr):
        #     if len(arr) == 1:
        #         return arr
            
        #     mid = len(arr) //2

        #     left = mergeSort(arr[:mid])
        #     right = mergeSort(arr[mid:])

        #     return merge(left,right)

        # def merge(left, right):
        #     res = []
        #     l, r = 0, 0
        #     while l < len(left) and r < len(right):
        #         if left[l] <= right[r]:
        #             res.append(left[l])
        #             l += 1
        #         else:
        #             res.append(right[r])
        #             r += 1
            
        #     while l < len(left):
        #         res += left[l:]

        #     while r < len(right):
        #         res += right[r:]

        #     return res
        
        # return mergeSort(nums)

        








