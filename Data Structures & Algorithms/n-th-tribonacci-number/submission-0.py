class Solution:
    def tribonacci(self, n: int) -> int:
        t0=0
        t1=1
        t2=1
        if n==0:
            return 0
        elif n==1:
            return 1
        elif n==2:
            return 1
        curr=0
        for i in range(3,n+1):
            curr=t0+t1+t2
            prev2=t2
            t2=curr
            prev1=t1
            t1=prev2
            t0=prev1
        return curr

