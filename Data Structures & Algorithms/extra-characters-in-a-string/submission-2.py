class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n=len(s)
        words= set(dictionary)
        dp= [-1 for _ in range(len(s)+1)]
        dp[len(s)]=0
        
        for i in range(n-1,-1,-1):
            dp[i]=1+dp[i+1]
            for j in range(i,len(s)):
                if s[i:j+1] in words:
                    dp[i]=min(dp[i],dp[j+1])

        return dp[0]