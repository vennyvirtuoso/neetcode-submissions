class Solution:
    def hammingWeight(self, n: int) -> int:
        ans=0
        # ans+=(1&(n>>1))
        i=0
        while n>>i>0:
            ans+=(1&(n>>i))
            i+=1
        return ans