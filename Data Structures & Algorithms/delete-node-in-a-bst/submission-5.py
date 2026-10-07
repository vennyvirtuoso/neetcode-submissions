# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        parent = None
        temp=root
        while temp:
            if key<temp.val:
                parent=temp
                temp=temp.left
            elif key>temp.val:
                parent=temp
                temp=temp.right
            else:
                break
        curr=temp
        if temp==None:
            return root
        if not curr.left:
            if curr==root:
                return curr.right
            if parent.left==curr:
                parent.left=curr.right
            else:
                parent.right=curr.right
        elif not curr.right:
            if curr==root:
                return curr.left
            if parent.left==curr:
                parent.left=curr.left
            else:
                parent.right=curr.left
        if curr.right:
            curr= curr.right
        while curr.left:
            curr=curr.left
        curr.left=temp.left
        if parent==None :
            return temp.right
        if temp.val>parent.val:
            parent.right=temp.right
        if temp.val<parent.val:
            parent.left=temp.right
        return root

