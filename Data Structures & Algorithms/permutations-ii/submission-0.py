class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        # ans=[]
        used= [0]*n
        trace=set()
        def permute(curr):
            if len(curr)==n:
                # ans.append(curr.copy())
                trace.add(tuple(curr.copy()))
            else:
                for i in range(n):
                    if not used[i]:
                        curr.append(nums[i])
                        used[i]=1
                        permute(curr)
                        used[i]=0
                        curr.pop()





        permute([])
        return list(trace)
