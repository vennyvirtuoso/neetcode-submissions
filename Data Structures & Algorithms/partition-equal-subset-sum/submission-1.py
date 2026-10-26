class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total=0
        n=len(nums)
        for i in range(n):
            total+=nums[i]
        dp = [[-1] * (total + 1) for _ in range(n)]


        def dfs(index,sum1):
            if index==n:
                return False
            if dp[index][sum1]!=-1:
                return dp[index][sum1]
            sum2=total-sum1
            temp1,temp2=False,False
            if sum1==sum2:
                return True
            else:
                temp1=dfs(index+1,sum1+nums[index])
                temp2=dfs(index+1,sum1)
            dp[index][sum1]=temp1 or temp2
            return temp1 or temp2

        return dfs(0,0)