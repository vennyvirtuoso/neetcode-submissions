class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n=len(nums)
        ans=max(nums)
        curr=0

        for i in range(0,n):
            if curr<0:
                curr=0
            curr+=nums[i]
            ans=max(ans,curr)
        globalmin=nums[0]
        currmin=0
        total=0
        for i in range(n):
            currmin=min(currmin+nums[i],nums[i])
            total+=nums[i]
            globalmin=min(globalmin,currmin)
        if ans>0:
            return max(ans,total-globalmin)
        else:
            return ans

            
        