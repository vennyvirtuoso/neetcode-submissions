class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[[-1]*n for _ in range(m)]
        def ways(i,j):
            if dp[i][j]!=-1:
                return dp[i][j]
            if i==m-1 and j==n-1:
                return 1
            else:

                temp1,temp2=0,0
                if i+1<m:
                    temp1=ways(i+1,j)
                if j+1<n:
                    temp2=ways(i,j+1)

                dp[i][j]=temp1+temp2
                return dp[i][j]
        ans= ways(0,0)

        return ans
        