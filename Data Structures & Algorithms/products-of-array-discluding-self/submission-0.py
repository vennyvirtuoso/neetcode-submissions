class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pl = []
        currpl = 1
        for num in nums:
            currpl = currpl*num
            pl.append(currpl)
        pr = [0 for _ in range(len(nums))]
        currpr = 1
        for i in range(len(nums)-1,-1,-1):
            currpr = currpr*nums[i]
            pr[i]=currpr
        ans=[0 for _ in range(len(nums))]
        for i in range(len(nums)):
            product = 1
            if i!=len(nums)-1:
                product=product*pr[i+1]
            if i!=0:
                product=product*pl[i-1]
            ans[i]=product

        return ans