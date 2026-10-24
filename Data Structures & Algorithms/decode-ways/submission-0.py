class Solution:
    def numDecodings(self, s: str) -> int:
        # number of ways
        dp=[0]*(len(s)+1)
        n= len(s)
        dp[n]=1
        for i in range(n-1,-1,-1):
            if s[i]=='0':
                dp[i]=0
            else:
                num= int(s[i:i+2])
                if 10<=num<=26:
                    dp[i]=dp[i+1]+dp[i+2]
                else:
                    dp[i]=dp[i+1]
        return dp[0]



        