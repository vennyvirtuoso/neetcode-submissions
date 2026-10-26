class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        dp = [[-1] * 2001 for _ in range(n + 1)]


        n=len(nums)
        def dfs(index,maxx):

            if index==n:
                return 0
            if dp[index][maxx+1000]!=-1:
                return dp[index][maxx+1000]
            ans=0
            temp1,temp2=0,0
            if nums[index]>maxx:
                temp1=1+dfs(index+1,nums[index])
            temp2=dfs(index+1,maxx)
            ans=max(temp1,temp2)
            dp[index][maxx+1000]=ans
            return ans
        return dfs(0,-1000)



        