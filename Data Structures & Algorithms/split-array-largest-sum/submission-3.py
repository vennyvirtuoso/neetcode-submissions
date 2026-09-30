class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left = max(nums)
        right = sum(nums)

        def possible(cand):
            splits=1
            temp=0
            for i in range(len(nums)):
                if temp+nums[i]<=cand:
                    temp+=nums[i]
                else:
                    temp=nums[i]
                    splits+=1

            return splits<=k


        ans=right
        while left<=right:

            cand= left+(right-left)//2
            if possible(cand):
                ans=cand
                right=cand-1
            else:
                left=cand+1



        return ans