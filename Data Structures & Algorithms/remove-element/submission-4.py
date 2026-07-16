class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ans=0
        for i, num in enumerate(nums):
            if nums[i]==val:
                ans+=1
                j=len(nums)-1
                while j>i and (nums[j]==val or nums[j]==-1) :
                    j-=1
                if j>0:
                    # print("yes")
                    nums[i]=nums[j]
                    nums[j]=-1
                    
        # print(nums)
        return len(nums)-ans