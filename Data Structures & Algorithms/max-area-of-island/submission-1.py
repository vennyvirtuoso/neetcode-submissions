class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        mask=[[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        m=len(grid)
        n=len(grid[0])
        area=0
        def dfs(i,j):
            if i>=0 and j>=0 and i<m and j<n:
                if grid[i][j]==1 and not mask[i][j]:
                    mask[i][j]=1
                    return 1+dfs(i-1,j)+dfs(i+1,j)+dfs(i,j+1)+dfs(i,j-1)
            return 0

        for i in range(m):
            for j in range(n):
                if grid[i][j]==1 and not mask[i][j]:
                    area=max(area,dfs(i,j))
        return area