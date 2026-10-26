class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n=len(s)
        dp= [False]*n
        wordDict=set(wordDict)
        memo={}
        def dfs(index):
            if index==n:
                return True
            if index in memo:
                return memo[index]

            temp=""
            for i in range(index,n):
                temp+=s[i]

                if temp in wordDict:
                    
                    if dfs(i+1):
                        memo[index]=True
                        return True
            memo[index]=False
            return False



        return dfs(0)



