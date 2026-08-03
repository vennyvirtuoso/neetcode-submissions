class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # selection sort
        n = len(nums)
        for i in range(1,n):
            for j in range(0,i):
                if nums[j]>nums[i]:
                    numm=nums[i]
                    for k in range(i,j,-1):
                        nums[k]=nums[k-1]
                    nums[j]=numm
        return nums