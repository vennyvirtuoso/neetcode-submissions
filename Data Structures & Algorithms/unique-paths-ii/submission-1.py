class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        dp=[[-1]*n for _ in range(m)]
        def ways(i,j):
            if dp[i][j]!=-1:
                return dp[i][j]
            if i==m-1 and j==n-1:
                return 1
            else:

                temp1,temp2=0,0
                if i+1<m and obstacleGrid[i+1][j]!=1:
                    temp1=ways(i+1,j)
                if j+1<n and obstacleGrid[i][j+1]!=1:
                    temp2=ways(i,j+1)

                dp[i][j]=temp1+temp2
                return dp[i][j]
        ans=0
        if obstacleGrid[0][0]!=1:
            ans= ways(0,0)
        

        return ans
        