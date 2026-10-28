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
        if not head:
            return None
        cur = head
        retrive = {}

        while cur:
            retrive[cur] = Node(cur.val)
            cur = cur.next

        #create random pointer for each new node
        cur = head
        while cur:
            retrive[cur].next = retrive.get(cur.next)
            retrive[cur].random = retrive.get(cur.random)
            cur = cur.next
            
        return retrive[head]






        