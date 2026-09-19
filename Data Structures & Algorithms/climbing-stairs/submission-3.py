class Solution:
    
    def climbStairs(self, n: int) -> int:
        count = [0 for _ in range(46)]
        count[1]=1
        count[2]=2
        for i in range(3,n+1):
            count[i]=count[i-2]+count[i-1]
        
        # print(count)
        return count[n]