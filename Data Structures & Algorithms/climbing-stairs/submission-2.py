class Solution:
    
    def climbStairs(self, n: int) -> int:
        count = [0 for _ in range(46)]
        count[1]=1
        count[2]=2
        def countw(n):
            print(n)
            if count[n]:
                return count[n]
            else:
                count[n]=countw(n-1)+countw(n-2)
                return count[n]
        
        print(count)
        return countw(n)