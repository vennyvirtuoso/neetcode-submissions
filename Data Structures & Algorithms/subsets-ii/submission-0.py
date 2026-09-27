class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        n=len(nums)
        nums.sort()

        def subset(i,curr):
            if i==n:
                ans.append(curr.copy())
            else:
                curr.append(nums[i])
                subset(i+1,curr)
                curr.pop()
                while i<n-1 and nums[i]==nums[i+1]:
                    i=i+1
                subset(i+1,curr)
        subset(0,[])
        return ans
