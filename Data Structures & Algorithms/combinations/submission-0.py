class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans=[]
        def takenottake(i,curr,len):
            if len==k:
                ans.append(curr.copy())

            elif i<=n:
                curr.append(i)
                # print(n)
                takenottake(i+1,curr,len+1)
                curr.pop()
                takenottake(i+1,curr,len)
                
        takenottake(1,[],0)
        return ans

