# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        cur = head
        i = 0
        #get length of the list
        while cur:
            i += 1
            cur = cur.next
        #edge cases
        
        if i <= 2:
            return 
        #divide list into 2 parts
        list1 = head
        i2 = 1
        while list1.next:
            if i2 == i//2:
                list2 = list1.next
                list1.next = None 
            else:
                list1 = list1.next
                list2 = list1.next
                i2 +=  1
            
        
        #reverse list2
        prev = None
        cur = list2
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        list2 = prev

        
        #merge 2 lists
        list1 = head
        while list1 and list2:
            temp1 = list1.next
            temp2 = list2.next
            list1.next = list2
            if temp1:
                list1.next.next = temp1
            else:
                list1.next.next = temp2           
            list1 = temp1
            list2 = temp2
        
            
            




        