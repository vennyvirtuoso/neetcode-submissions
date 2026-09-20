class Solution:
    def isHappy(self, n: int) -> bool:
        def SumSquare(n:int)->int:
            sum=0
            while n:
                ldigit=n%10
                sum+=(ldigit**2)
                n=n//10
            return sum
        cycle = set()
        while n not in cycle:
            cycle.add(n)
            n= SumSquare(n)
            if n==1:
                return True
        return False


        