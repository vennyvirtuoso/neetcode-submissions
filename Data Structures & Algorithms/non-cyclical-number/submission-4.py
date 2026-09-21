class Solution:
    def isHappy(self, n: int) -> bool:
        def SumSquare(n:int)->int:
            sum=0
            while n:
                ldigit=n%10
                sum+=(ldigit**2)
                n=n//10
            return sum


        fast=SumSquare(n)
        fast=SumSquare(fast)
        slow =SumSquare(n)
        while fast!=slow:
            slow =SumSquare(slow)
            fast=SumSquare(fast)
            fast=SumSquare(fast)
            # print(fast)
            if fast==1 or slow==1:
                return True
        if fast==1:
            return True
        else:
            return False


        