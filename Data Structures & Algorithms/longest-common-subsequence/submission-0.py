class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m=len(text1)
        n=len(text2)

        dp=[[-1]*n for _ in range(m)]
        def dfs(i,j):
            temp1,temp2,temp3=0,0,0
            if i<m and j<n and dp[i][j]!=-1:
                return dp[i][j]
            else:
                if i<m and j<n:
                    if text1[i]==text2[j]:
                        temp1 = 1+dfs(i+1,j+1)
                    temp2=dfs(i+1,j)
                    temp3=dfs(i,j+1)
                    dp[i][j]= max(temp1,temp2,temp3)
                    return dp[i][j]
                else:
                    return 0
            
        return dfs(0,0)
