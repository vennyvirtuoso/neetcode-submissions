class Solution:
    def rob(self, nums: List[int]) -> int:
        dp=[-1]*len(nums)
        def maxmoney(i):

            if i>=len(nums):
                return 0
            if dp[i]!=-1:
                return dp[i]


            dp[i]= max(nums[i]+maxmoney(i+2),maxmoney(i+1))
            return dp[i]
        return maxmoney(0)
        return dp[0]