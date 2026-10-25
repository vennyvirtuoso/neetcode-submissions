class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dpmax=[float('-inf')]*(len(nums))
        dpmin=[float('inf')]*(len(nums))
        dpmax[0],dpmin[0]=nums[0],nums[0]
        for i in range(1,len(nums)):
            dpmax[i]=max(nums[i],dpmax[i-1]*nums[i],dpmin[i-1]*nums[i])
            dpmin[i]=min(nums[i],dpmin[i-1]*nums[i],dpmax[i-1]*nums[i])

        return max(dpmax)
