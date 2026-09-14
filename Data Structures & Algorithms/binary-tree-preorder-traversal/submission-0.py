# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorder(self, node,ans):
        if node:
            ans.append(node.val)
        if node and node.left:
            temp = self.preorder(node.left,ans)
            if temp:
                ans.append(temp)
        if node and node.right:
            temp = self.preorder(node.right,ans)
            if temp:
                ans.append(temp)
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        self.preorder(root,ans)
        return ans