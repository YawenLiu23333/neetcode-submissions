# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def post(node):
            if node == None:
                return None
            left = post(node.left) 
            right = post(node.right) 

            node.left, node.right = right, left

            return node
        
        return post(root)
            
            