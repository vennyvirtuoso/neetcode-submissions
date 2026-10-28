class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        n=len(nums)
        dp={}
        def dfs(i,target):
            if i==n and target==0:
                return 1
            elif i==n:
                return 0
            if (i,target) in dp:
                return dp[(i,target)]
            else:
                plus=dfs(i+1,target-nums[i])
                minus=dfs(i+1,target+nums[i])
                dp[(i,target)]=plus+minus
                return dp[(i,target)]
        return dfs(0,target)
        