# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = head
        while n > 1:
            cur = cur.next
            n -= 1
        last = cur
        
        cur = head
        prev = None
        while last.next:
            last = last.next
            prev = cur
            cur = cur.next
        if prev:
            prev.next = cur.next
            return head
        else:
            return head.next


            
