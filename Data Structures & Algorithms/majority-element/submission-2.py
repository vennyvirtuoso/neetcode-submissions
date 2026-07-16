class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        INF = float('inf')
        i=0
        j=1
        n= len(nums)
        while(i<n and j<n):
            if nums[i]!=nums[j] and nums[i]!=INF and nums[j]!=INF:
                nums[i]=INF
                i=i+1
                nums[j]=INF
                j=j+1
            if i<n and nums[i]==INF:
                i=i+1
            if j<n and nums[j]==INF:
                j=j+1
            if i<n and j<n and nums[i]==nums[j]:
                j=j+1

        for num in nums:
            if num!=INF:
                return num
            