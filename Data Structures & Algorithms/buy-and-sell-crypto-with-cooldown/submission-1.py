class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n=len(prices)
        dp=[[-1,-1] for _ in range(n)]

        def dfs(i,buying):
            if i>=n:
                return 0
            if dp[i][buying]!=-1:
                return dp[i][buying]

            if buying==1:
                buy,sell=0,0
                buy = -prices[i]+dfs(i+1,0)
                skip = dfs(i+1,1)
                dp[i][buying]=max(buy,skip)
                return dp[i][buying]
            if buying ==0:
                sell,skip=0,0
                sell=prices[i]+dfs(i+2,1)
                skip=dfs(i+1,0)
                dp[i][buying]=max(sell,skip)
                return dp[i][buying]

        return dfs(0,1)

            