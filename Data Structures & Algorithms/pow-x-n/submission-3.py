class Solution:

            
    def myPow(self, x: float, n: int) -> float:
        def pow(x,n):
            if x==0:
                return 0
            if n==0:
                return 1
            if n%2==0:
                res= pow(x*x,n//2)
                return res
            else:
                res= pow(x*x,n//2)
                res=res*x
                return res
        res= pow(x,abs(n))
        if n>=0:
            return res
        else: return 1/res

