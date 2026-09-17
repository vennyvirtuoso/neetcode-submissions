class Solution:

    def subsetXORSum(self, nums: List[int]) -> int:
        ans=0
        n = len(nums)
        for mask in range(1<<n):
            temp=0
            for i in range(n):
                if mask & (1<<i):
                    temp=temp^nums[i]
            ans+=temp
        return ans