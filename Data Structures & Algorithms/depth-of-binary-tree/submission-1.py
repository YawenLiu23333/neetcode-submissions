# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        depth = 0
        def dfs(root, level):
            nonlocal depth
            if root is None:
                return 
            if depth == level:
                depth += 1
            dfs(root.left, level + 1)
            dfs(root.right, level + 1)
        dfs(root, 0)
        return depth 
            
            
            