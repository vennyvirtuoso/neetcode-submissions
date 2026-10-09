class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n=len(nums)
        maxb=max(nums)
        minb=min(nums)
        if n==1:
            return nums[0]
        for i in range(1,n):
            nums[i]+=nums[i-1]

        maxx=max(nums)
        minn=min(nums)
        if maxx>=0 and minn<=0:
            return maxx-minn
        if maxx>=0 and minn>=0:
            return maxx
        if maxb<0 and minb<0:
            return maxb
        else:
            return maxx-minn

