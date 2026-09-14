# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invert(self,node):
        if node and node.left:
            self.invert(node.left)
        if node and node.right:
            self.invert(node.right)
        if node:
            node.left,node.right=node.right,node.left
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.invert(root)
        return root