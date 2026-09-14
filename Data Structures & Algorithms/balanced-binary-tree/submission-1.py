# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def Balanced(self,node,ans):
        ls=0
        rs=0
        if node:

            if node.left:
                ls = self.Balanced(node.left,ans)+1
            if node.right:
                rs = self.Balanced(node.right,ans)+1
        ans[0]=max(ans[0],abs(ls-rs))
        return max(ls,rs)


            

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        ans=[0]
        self.Balanced(root,ans)
        if ans[0]>1:
            return False
        return True