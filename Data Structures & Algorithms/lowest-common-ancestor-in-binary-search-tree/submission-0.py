# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        temp=root
        if p.val>q.val:
            p,q=q,p
        while temp:
            if p.val==temp.val or q.val==temp.val or p.val<temp.val<q.val:
                return temp
            elif p.val<q.val<temp.val:
                temp=temp.left
            else:
                temp=temp.right
        
        return a