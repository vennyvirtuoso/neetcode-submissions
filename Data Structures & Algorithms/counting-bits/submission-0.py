class Solution:
    def countBits(self, n: int) -> List[int]:
        def count(n):
            ans=0
            i=0
            while n>>i>0:
                ans+=(1&n>>i)
                i+=1
            return ans
        ans=[]
        for i in range(n+1):
            ans.append(count(i))
        return ans
