class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # print(n)
        for i in range(n-1,0,-1):
            # print(i)
            for j in range(0,i):
                if nums[j]>nums[j+1]:
                    nums[j],nums[j+1]=nums[j+1],nums[j]
        return nums