class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        ans=[]
        while i<len(nums)-1:
            if nums[i]!=nums[i+1]:
                ans.append(nums[i])
            i+=1
        # if nums[len(nums)-2]!=nums[len(nums)-1]:
        ans.append(nums[len(nums)-1])
        nums[:len(ans)]=ans
        return len(ans)