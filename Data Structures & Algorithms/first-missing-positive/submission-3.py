class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(len(nums)):
            while i+1!=nums[i] and nums[i]>0 and nums[i]<n:

                j=nums[i]
                if nums[i]==nums[j-1]:
                    break;
                # print(nums[i])
                nums[i],nums[j-1]=nums[j-1],nums[i]

        # print(nums)
        for i in range(n):
            if i+1!=nums[i]:
                return i+1
        return n+1