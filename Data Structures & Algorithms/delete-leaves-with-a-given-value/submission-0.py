# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def remove(node):
            if not node.left and not node.right:
                if node.val==target:
                    return None
                else:
                    return node
            if node.left:
                node.left=remove(node.left)
            if node.right:
                node.right=remove(node.right)

            if not node.left and not node.right:
                if node.val==target:
                    return None
            return node

        temp=remove(root)
        if not temp:
            return temp
        if temp.val==target:
            return None
        return root