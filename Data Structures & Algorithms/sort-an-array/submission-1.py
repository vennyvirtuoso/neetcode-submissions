class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # selection sort
        n = len(nums)
        for i in range(0,n-1):
            min_i=i
            minn = nums[i]
            for j in range(i,n):
                if minn>nums[j]:
                    minn = min(minn,nums[j])
                    min_i=j
            nums[i],nums[min_i]=nums[min_i],nums[i]
        return nums