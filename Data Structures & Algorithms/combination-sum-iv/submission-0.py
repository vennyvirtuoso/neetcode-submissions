class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp=[-1]*(target+1)
        def dfs(remaining):
            if remaining<0:
                return 0
            if remaining==0:
                return 1
            if dp[remaining]!=-1:
                return dp[remaining]
            nw=0
            for num in nums:
                nw+=(dfs(remaining-num))

            dp[remaining]=nw
            return nw
        return dfs(target)

        