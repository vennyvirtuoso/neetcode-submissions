class Solution:
    def isHappy(self, n: int) -> bool:
        num=str(n)
        sum=0
        loop=10
        while sum!=1 and loop:
            sum=0
            # print(sum)
            for i in range(len(num)):
                sum+=(int(num[i])**2)
            num=str(sum)
            loop-=1
        return True and bool(loop)

        