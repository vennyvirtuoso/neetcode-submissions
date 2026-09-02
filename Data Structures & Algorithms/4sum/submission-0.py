class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        count = dict()
        ans=[]
        for i in range(n):
            count[nums[i]]=count.get(nums[i],0)+1
        
        for i in range(n):
            count[nums[i]]-=1
            if i and nums[i]==nums[i-1]:
                continue
            
            
            for j in range(i+1,n):
                count[nums[j]]-=1
                if j-1>i and nums[j] == nums[j-1]:
                    continue
                
                for k in range(j+1,n):
                    count[nums[k]]-=1
                    if k-1>j and nums[k]==nums[k-1]:
                        continue
                    
                    targett = target-(nums[i]+nums[j]+nums[k])
                    if count.get(targett,0)>0:
                        ans.append([nums[i],nums[j],nums[k],targett])

                for k in range(j+1,n):
                    count[nums[k]]+=1


            for j in range(i+1,n):
                count[nums[j]]+=1
        
        return ans

            