# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameter(self,node,ans):
        lh=0
        rh=0
        if node:
            if node.left:
                lh = self.diameter(node.left,ans)+1
            if node.right:
                rh = self.diameter(node.right,ans)+1
        ans[0]=max(ans[0],lh+rh)
        # print(ans[0])
        # print(lh)
        # print(rh)
        return max(lh,rh)
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans=[0]
        self.diameter(root,ans)
        return ans[0]
