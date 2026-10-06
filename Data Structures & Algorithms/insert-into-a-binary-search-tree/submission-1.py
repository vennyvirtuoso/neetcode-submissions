# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        temp=root
        node=TreeNode(val)
        while temp:
            if val>temp.val:
                if not temp.right:
                    temp.right=node
                    break
                else:
                    temp=temp.right
            elif val<temp.val:
                if not temp.left:
                    temp.left=node
                    break
                else:
                    temp=temp.left
        if not temp:
            return node
        return root
                    