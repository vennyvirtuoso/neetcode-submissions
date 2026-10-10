class Solution:
    def jump(self, nums: List[int]) -> int:
        maxreach=0
        jump=0
        currmax=0
        for i in range(len(nums)):
            maxreach=max(maxreach,i+nums[i])
            if i==currmax and not i==len(nums)-1:
                currmax=maxreach
                jump+=1

            

        return jump