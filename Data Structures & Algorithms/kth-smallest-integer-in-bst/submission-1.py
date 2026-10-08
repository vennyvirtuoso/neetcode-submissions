# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self, k=0, compare=0):
        self.k = k
        self.compare = compare

    def dfs(self, root):
        if root is None:
            return root
        
        temp=self.dfs(root.left)
        if temp is not None:
            return temp
        
        self.compare+=1
        if self.compare == self.k:
            return root.val
        temp=self.dfs(root.right)
        if temp is not None:
            return temp

        return None

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        return self.dfs(root)