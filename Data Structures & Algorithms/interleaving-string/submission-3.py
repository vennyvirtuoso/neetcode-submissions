class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n=len(s1)
        m=len(s2)
        k=len(s3)
        if n+m!=k:
            return False


        dp =[[-1 for _ in range(m+1)] for _ in range(n+1)]

        def bfs(i,j):
            if i==n and j==m:
                return True
            if dp[i][j]!=-1:
                return dp[i][j]
            temp1,temp2=False,False

            if i<n and s1[i]==s3[i+j]:
                temp1=bfs(i+1,j)
                
            if j<m and s2[j]==s3[i+j]:
                temp2=bfs(i,j+1)

            dp[i][j]=temp1 or temp2
            return dp[i][j]

        # print(dp)
        return bfs(0,0)

