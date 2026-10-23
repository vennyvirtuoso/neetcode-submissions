class Solution:
    def rob(self, nums: List[int]) -> int:
        dp1=[-1]*len(nums)
        dp2=[-1]*len(nums)
        n=len(nums)
        if n==1:
            return nums[0]
        def money1(i):
            if i>=n-1:
                return 0
            if dp1[i]!=-1:
                return dp1[i]

            dp1[i]=max(nums[i]+money1((i+2)),money1((i+1)))
            return dp1[i]
        def money2(i):
            if i>=n:
                return 0
            if dp2[i]!=-1:
                return dp2[i]

            dp2[i]=max(nums[i]+money2((i+2)),money2((i+1)))
            return dp2[i]
        money1(0)
        money2(1)
        return max(dp1[0],dp2[1])
        
        