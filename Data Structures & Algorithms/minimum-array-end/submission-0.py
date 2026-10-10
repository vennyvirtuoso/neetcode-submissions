class Solution:
    def minEnd(self, n: int, x: int) -> int:
        b=n-1
        temp=x
        pow=0
        ans=0
        while b:
            ld=1&temp
            if ld==1:
                pow+=1
                temp=temp>>1
            else:
                ldb=1&b
                ans+=(ldb*(2**pow))
                b=b>>1
                pow+=1
                temp=temp>>1
        # print(ans)
        return ans+x