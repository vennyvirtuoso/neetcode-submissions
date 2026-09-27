class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        ans=[]
        nums.sort()
        used= [0]*n
        # trace=set()
        def permute(curr):
            if len(curr)==n:
                ans.append(curr.copy())
                # trace.add(tuple(curr.copy()))
            else:
                for i in range(n):
                    if not used[i]:
                        if i>0 and nums[i]==nums[i-1] and not used[i-1]:
                            continue
                        curr.append(nums[i])
                        used[i]=1
                        permute(curr)

                        used[i]=0
                        curr.pop()






        permute([])
        # return list(trace)
        return ans
