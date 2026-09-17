class Solution:

    def subsetXORSum(self, nums: List[int]) -> int:
        ans=0
        def backtrack(i,subset):
            res=0
            nonlocal ans
            for s in subset:
                res=res^s
            ans+=res
            for j in range(i,len(nums)):
                subset.append(nums[j])
                backtrack(j+1,subset)
                subset.pop()
        backtrack(0,[])
        return ans