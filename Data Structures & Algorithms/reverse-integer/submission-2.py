class Solution:
    def reverse(self, x: int) -> int:
        b=abs(x)
        ans=0
        pow=1
        c=b
        while c//pow>=10:
            pow*=10
        print(pow)
        while b:
            lastdigit=b%10
            b=b//10
            ans+=lastdigit*pow
            pow//=10
        int_max=0x7FFFFFFF
        if ans>int_max:
            return 0
        if x<0:
            return -ans
        return ans




        