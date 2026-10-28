"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        record = {}

        cur = head
        while cur:
            record[cur] = Node(cur.val)
            cur = cur.next

        cur = head
        while cur:
            record[cur].next = record.get(cur.next)
            record[cur].random = record.get(cur.random)
            cur = cur.next
        if head:
            return record[head]

        return None
        