class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        countt=dict()
        ans = []
        for i in range(len(nums)):
            countt[nums[i]]=countt.get(nums[i],0)+1
        # print(countt)

        i=0
        j=0
        while i<len(nums):
            countt[nums[i]]-=1
            if i and nums[i]==nums[i-1]:
                i+=1
                continue
            j=i+1
            while j<len(nums):
                countt[nums[j]]-=1
                if j-1>i and nums[j]==nums[j-1]:
                    j+=1
                    continue
                target = 0-nums[i]-nums[j]
                if countt.get(target,0)>0:
                    ans.append([nums[i],nums[j],target])
                j+=1

            # countt[nums[i]]=countt.get(nums[i],0)+1
            for j in range(i+1,len(nums)):
                countt[nums[j]]+=1
            i+=1

                    

        return ans



                