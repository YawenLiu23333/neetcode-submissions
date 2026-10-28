# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, low, high):
            if root is None:
                return True
            
            if root.val >= low or root.val <= high:
                return False

            left = dfs(root.left, root.val, high)
            right = dfs(root.right, low, root.val)

            return left and right

        res = dfs(root, float('inf'), -float('inf'))
        return res

        