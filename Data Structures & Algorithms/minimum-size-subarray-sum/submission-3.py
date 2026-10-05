class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i=0
        j=0
        sum=0
        ans=float('inf')
        while i<len(nums):
            if sum<target:
                sum+=nums[i]
                i+=1

            while sum>=target:
                # print(sum)
                # print(target)
                # print(i)
                # print(j)
                ans=min(ans,i-j)
                sum-=nums[j]
                j+=1



        return 0 if ans==float('inf') else ans
            