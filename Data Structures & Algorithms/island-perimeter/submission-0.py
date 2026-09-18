class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        neigh=0
        total=0
        m = len(grid)
        n=len(grid[0])
        # print(m)
        # print(n)
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    total+=1
                if grid[i][j]==1 and j<n-1 and grid[i][j+1]==1:
                    neigh+=1
                if grid[i][j]==1 and i<m-1 and grid[i+1][j]==1:
                    neigh+=1
        # print(neigh)
        return 4*total-2*neigh