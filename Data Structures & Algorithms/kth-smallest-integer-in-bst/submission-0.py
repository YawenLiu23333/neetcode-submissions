# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = k
        res = None
        def dfs(root):
            nonlocal count, res
            if root is None:
                return 0
            left = dfs(root.left)
            print(root.val)
            count -= 1
            if count == 0:
                res = root.val
            right = dfs(root.right)
            if res != None:
                return res
        res = dfs(root)
        return res
            

       
