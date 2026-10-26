class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])

        dp=[[-1]*n for _ in range(m)]

        def minsum(i,j):
            if dp[i][j]!=-1:
                return dp[i][j]
            if i==m-1 and j==n-1:
                return grid[i][j]
            else:
                temp1,temp2=float('inf'),float('inf')
                if i+1<m:
                    temp1=minsum(i+1,j)
                if j+1<n:
                    temp2=minsum(i,j+1)
                dp[i][j]=grid[i][j]+min(temp1,temp2)
                return dp[i][j]

            
        return minsum(0,0)
                    
        