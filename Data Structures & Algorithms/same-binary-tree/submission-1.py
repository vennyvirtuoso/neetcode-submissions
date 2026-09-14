# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def same(self,p,q,ans):
        if p and q:
            if p.val!=q.val:
                ans[0]=False
            if p.left and q.left:
                ls= self.same(p.left,q.left,ans)
            elif p.left or q.left:
                ans[0]=False
            if p.right and q.right:
                rs= self.same(p.right,q.right,ans)
            elif p.right or q.right:
                ans[0]=False
        elif p or q:
            ans[0]=False

            
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        ans=[True]
        temp=self.same(p,q,ans)
        return ans[0]
        
