class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        summ=0
        for i in range(len(stones)):
            summ+=stones[i]
        tar=summ//2
        n=len(stones)

        dp=[[-1]*(tar+1) for _ in range(n)]
        def dfs(i,target):

            if target==0 or i==n:
                return 0
            if dp[i][target]!=-1:
                return dp[i][target]
            take=0
            if target>=stones[i]:
                take= stones[i]+dfs(i+1,target-stones[i])
            skip= dfs(i+1,target)
            dp[i][target]=max(take,skip)
            return dp[i][target]
        print(tar)
        x=dfs(0,tar)
        return summ-2*x



