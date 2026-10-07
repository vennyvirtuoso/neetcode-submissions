# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self,ans=0):
        self.ans=0
    
    def goodNodes2(self,maxx,node):
        if node:
            if maxx<=node.val:
                self.ans+=1
        maxx=max(maxx,node.val)
        if node.left:
            self.goodNodes2(maxx,node.left)
        if node.right:
            self.goodNodes2(maxx,node.right)
    def goodNodes(self, root: TreeNode) -> int:
        maxx=root.val
        self.goodNodes2(maxx,root)
        return self.ans