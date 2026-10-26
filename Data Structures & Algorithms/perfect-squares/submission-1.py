import math
class Solution:
    def numSquares(self, n: int) -> int:
        dp=[-1]*(n+1)
        def dfs(n):
            if n<0:
                return float('inf')
            if n==1 or n==0:
                return n
            if dp[n]!=-1:
                return dp[n]
            ln=float('inf')
            for i in range(math.isqrt(n)+1,0,-1):
                ln=min(ln,1+dfs(n-i**2))
            dp[n]=ln
            return ln
        return dfs(n)


        