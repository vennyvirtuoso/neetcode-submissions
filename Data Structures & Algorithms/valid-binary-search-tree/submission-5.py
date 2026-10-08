# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self,ans=True):
        self.ans=ans
    def isvalidl(self,root,rangee):
        # print(rangee)
        rang1=rangee.copy()
        rang2=rangee.copy()
        if root:
            if not(root.val>rangee[0]):
                self.ans=False
            if not (root.val<rangee[1]):
                self.ans=False
            
            if root.left:
                rang1[1]=min(rangee[1],root.val)
                # print(rang1)
                self.isvalidl(root.left,rang1)

            if root.right:

                rang2[0]=max(rangee[0],root.val)
                # print(rang2)
                # print(rang2)
                self.isvalidl(root.right,rang2)



        
    def isValidBST(self, root: Optional[TreeNode]) -> bool:


        self.isvalidl(root,[float('-inf'),float('inf')])
        return self.ans

            
                    