class Solution:
    
    def climbStairs(self, n: int) -> int:
        ways=[-1]*(n)

        def dfs(i):
            if i>=n:
                return i==n
            if ways[i]!=-1:
                return ways[i]
            ways[i]=dfs(i+1)+dfs(i+2)
            return ways[i]
        dfs(0)
        return ways[0]



