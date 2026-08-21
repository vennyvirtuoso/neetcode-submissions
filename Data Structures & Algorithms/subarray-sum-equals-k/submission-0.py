class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dictt = dict()
        dictt[0]=1
        for i in range(1,len(nums)):
            nums[i]+=nums[i-1]
        ans=0
        for prefixsum in nums:
            if prefixsum-k in dictt:
                ans+=dictt[prefixsum-k]
            if prefixsum in dictt:
                dictt[prefixsum]+=1
            else:
                dictt[prefixsum]=1
        return ans