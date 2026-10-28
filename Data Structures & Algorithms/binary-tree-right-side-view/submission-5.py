# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def dfs(root, level):
            nonlocal res 
            if root is None:
                return
            if level == len(res):
                res.append(root.val)


            right = dfs(root.right, level + 1)
            left = dfs(root.left, level + 1)

            return
        dfs(root, 0)
        return res




            

