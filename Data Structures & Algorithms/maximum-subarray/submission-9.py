class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n=len(nums)
        ans=max(nums)
        curr=0

        for i in range(0,n):
            if curr<0:
                curr=0
            curr+=nums[i]
            ans=max(ans,curr)
        return max(ans,curr)
            

