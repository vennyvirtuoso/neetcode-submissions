class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)
        mincost = [0]*(n+1)
        mincost[0]=0
        mincost[1]=0
        for i in range(2,n+1):
            
            mincost[i]=min((cost[i-1]+mincost[i-1]),(cost[i-2]+mincost[i-2]))
        return mincost[n]