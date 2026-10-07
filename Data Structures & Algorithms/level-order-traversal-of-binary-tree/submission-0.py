# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans=[]
        stack=deque()
        if root==None:
            return []
        stack.append(root)
        temp= deque()
        tempans=[]
        while len(stack)>0:
            tempnode=stack.popleft()
            if tempnode.left:
                temp.append(tempnode.left)
            if tempnode.right:
                temp.append(tempnode.right)



            tempans.append(tempnode.val)
            if len(stack)==0:
                stack=temp
                ans.append(tempans)
                temp= deque()
                tempans=[]
        return ans


