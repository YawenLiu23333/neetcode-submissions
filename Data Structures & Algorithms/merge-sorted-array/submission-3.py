class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1, p2 = m -1, n - 1
        insert = m + n - 1

        while insert >= 0:
            print('insert is at', insert)
            if p1 < 0:
                print(p2)
                nums1[insert] = nums2[p2]
                p2 -= 1
            elif p2 < 0:
                break
            elif nums1[p1] >= nums2[p2]:
                nums1[insert] = nums1[p1]
                p1 -= 1
            else:
                nums1[insert] = nums2[p2]
                p2 -= 1
            insert -= 1


            


            
       







        

            
        
        

        

