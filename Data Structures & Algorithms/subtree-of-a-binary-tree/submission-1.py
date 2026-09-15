# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution: 
    def SameTree(self,node,subRoot):
        if node and subRoot:
            ls=True
            rs=True
            if node.val != subRoot.val:
                return False
            if node.left and subRoot.left:
                ls= self.SameTree(node.left,subRoot.left)
            elif node.left or subRoot.left:
                return False
            if node.right and subRoot.right:
                rs= self.SameTree(node.right,subRoot.right)
            elif node.right or subRoot.right:
                return False
            return ls and rs
        if node or subRoot:
            return False
    def SubTree(self, node, subRoot):
        if node:
            ls=False
            rs=False
            if self.SameTree(node,subRoot):
                return True
            if node.left:
                ls= self.SubTree(node.left,subRoot)
            if node.right:
                rs= self.SubTree(node.right,subRoot)
            return ls or rs
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        return self.SubTree(root,subRoot)