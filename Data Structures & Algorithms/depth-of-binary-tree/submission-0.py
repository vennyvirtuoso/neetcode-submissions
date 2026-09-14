# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def depth(self,root):
        if root:
            temp1=0
            temp2=0
            if root.left:
                temp1= self.depth(root.left)+1
            if root.right:
                temp2=self.depth(root.right)+1
            return max(temp1,temp2)
        return 0
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root:
            return 1+self.depth(root)
        else:
            return 0
        # return self.depth(root)