# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        old = None
        cur = head
        while cur:
            new = cur.next
            cur.next = old
            old = cur
            cur = new
        return old


