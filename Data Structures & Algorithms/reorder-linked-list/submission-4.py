# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = slow = head
        while fast.next and fast.next.next:
            #why need both fast.next and fast.next.next
            slow = slow.next
            fast = fast.next.next
        
        new = slow.next
        slow.next = None
        old = None
        while new:
            #reverse second half
            temp = new.next
            new.next = old
            old = new
            new = temp
            #new head of reversed second list is old

        #link 2 lists together
        cur = head
        while cur and old:
            temp = cur.next
            temp2 = old.next

            cur.next = old
            old.next = temp

            cur = temp
            old = temp2




        








        