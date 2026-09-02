class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans=[]
        count = dict()
        for i in range(n):
            count[nums[i]]=count.get(nums[i],0)+1
        print(count)
        for i in range(n):
            count[nums[i]]-=1
            if i and nums[i]==nums[i-1]:
                continue
            for j in range(i+1,n):
                count[nums[j]]-=1
                if j-1>i and nums[j]==nums[j-1]:
                    continue
                target = -(nums[i]+nums[j])
                if count.get(target,0)>0:
                    ans.append([nums[i],nums[j],target])

            for j in range(i+1,n):
                count[nums[j]]+=1
        
        return ans