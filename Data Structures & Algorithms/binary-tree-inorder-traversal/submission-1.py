# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self, node,ans):
        if not node:
            return
        if node.left:
            temp=self.inorder(node.left,ans)
            if temp:
                ans.append(temp)
        if node:
            print(node.val)
            ans.append(node.val)
        if node.right:
            temp=self.inorder(node.right,ans)
            if temp:
                ans.append(temp)
        
        
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        self.inorder(root,ans)
        return ans