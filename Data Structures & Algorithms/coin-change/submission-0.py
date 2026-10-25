class Solution:
    
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[-1]*(amount+1)
        dp[0]=0

        def dfs(amount):
            if amount<0:
                return float('inf')
            elif dp[amount]!=-1:
                return dp[amount]

            temp=float('inf')
            for i in range(len(coins)):
                temp=min(temp,1+dfs(amount-coins[i]))
            
            dp[amount]=temp
            return dp[amount]
                
        dfs(amount)
        if dp[amount]==float('inf'):
             return -1
        else:
            return dp[amount]