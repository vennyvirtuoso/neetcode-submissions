class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n=len(s)
        dp=[False]*n
        dp[0]=True
        j=0
        i=0
        while i<n:
            # print(dp)
            if dp[i] and s[i]=="0":
                start=i+minJump
                end=i+maxJump
                dp[start:end+1]=[True]*(end+1-start)
            i+=1
        return dp[n-1] and not int(s[n-1])