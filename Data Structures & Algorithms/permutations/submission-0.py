class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        used = [0]*n
        ans=[]
        def perm(curr):
            if len(curr)==n:
                
                ans.append(curr.copy())
                return
            else:
                for i in range(n):
                    if not used[i]:
                        curr.append(nums[i])
                        used[i]=1
                        perm(curr)
                        used[i]=0
                        curr.pop()
        perm([])
        return ans