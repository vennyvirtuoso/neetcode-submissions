"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct2(self,n,grid):
        mask1= [[1 for _ in range(n)] for _ in range(n)]
        mask0= [[0 for _ in range(n)] for _ in range(n)]
        temp=Node()
        if mask1==grid:
            temp.isLeaf=1
            temp.val=1
            temp.topLeft = None
            temp.topRight = None
            temp.bottomLeft = None
            temp.bottomRight = None
        elif mask0==grid:
            temp.isLeaf=1
            temp.val=0
            temp.topLeft = None
            temp.topRight = None
            temp.bottomLeft = None
            temp.bottomRight = None
        else:
            temp.isLeaf=0
            temp.val=0
            mid = n // 2
            topLeft= [
                row[:mid]
                for row in grid[:mid]
            ]
            topRight= [
                row[mid:]
                for row in grid[:mid]
            ]
            bottomLeft= [
                row[:mid]
                for row in grid[mid:]
            ]
            bottomRight= [
                row[mid:]
                for row in grid[mid:]
            ]
            temp.topLeft = self.construct2(n//2,topLeft)
            temp.topRight = self.construct2(n//2,topRight)
            temp.bottomLeft = self.construct2(n//2,bottomLeft)
            temp.bottomRight = self.construct2(n//2,bottomRight)
        return temp
        
        

    def construct(self, grid: List[List[int]]) -> 'Node':
        n=len(grid)
        n=len(grid[0])
        return self.construct2(n,grid)




