class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        minimum = min(nums)
        mul = target//minimum
        ans=[]
        def combination(i,curr,total):
            if total==target:
                ans.append(curr.copy())
                return 
            elif total<target and i<len(nums):
                curr.append(nums[i])
                combination(i,curr,total+nums[i])
                curr.pop()
                combination(i+1,curr,total)
                




        combination(0,[],0)
        return ans