class Solution:
    def integerBreak(self, n: int) -> int:
        # if n==2:
        #     return 1
        dp=[-1]*(n+1)
        def dfs(n):
            if n==0:
                return 1
            if n==1:
                return 1

            if dp[n]!=-1:
                return dp[n]
            ans=float('-inf')
            for i in range(n,0,-1): 
                ans=max(ans,i*dfs(n-i))
            dp[n]=ans
            return ans

        ans=float('-inf')
        for i in range(n-1,0,-1):
            ans=max(ans,i*dfs(n-i))
        dp[n]=ans
        return dp[n]


        