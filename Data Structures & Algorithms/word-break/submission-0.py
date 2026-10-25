class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n=len(s)
        dp= [False]*n
        wordDict=set(wordDict)

        def dfs(index):
            temp=""
            ans=False
            if index<n:
                if dp[index]:
                    return dp[index]
            for i in range(index,n):
                temp+=s[i]
                # print(temp)
                if temp in wordDict:
                    dp[i]=True
                    dfs(i+1)


        dfs(0)
        # print(dp)
        

        return dp[n-1]


