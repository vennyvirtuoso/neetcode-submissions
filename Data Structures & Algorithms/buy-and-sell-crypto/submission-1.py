class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        ans=0
        for i in range(0,n):
            for j in range(i,n):
                ans = max(prices[j]-prices[i],ans)
        return ans