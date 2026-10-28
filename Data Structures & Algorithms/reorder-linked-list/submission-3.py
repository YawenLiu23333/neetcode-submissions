# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = slow = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        second = slow.next
        slow.next = None

        #reverse second half of list
        cur = None
        while second:
            temp = second
            second = second.next
            temp.next = cur
            cur = temp
        new = cur
        
        #merge 2 lists
        old = head
        while new:
            temp1 = old.next
            temp2 = new.next

            old.next = new
            new.next = temp1

            old = temp1
            new = temp2




            
            
            

