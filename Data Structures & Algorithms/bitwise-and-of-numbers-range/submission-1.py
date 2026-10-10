class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        diff=right-left

        pos=0
        start=1
        while start<=diff:
            pos+=1
            start=start*2
        mask=~((1<<pos)-1)
        return left&mask&right
        # return left

