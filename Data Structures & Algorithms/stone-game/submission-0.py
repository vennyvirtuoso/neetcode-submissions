class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles);
        dp= [[-1 for _ in range(n)] for _ in range(n)];
        def dfs(i,j,alice,bob,turn):
            if i>j:
                if alice>bob:
                    return True
                else:
                    return False
            if dp[i][j]!=-1:
                return dp[i][j];
            temp1,temp2=-1,-1;
            if turn:
                temp1=dfs(i+1,j,alice+piles[i],bob,0) | dfs(i,j-1,alice+piles[j],bob,0);
            else:
                temp2=dfs(i+1,j,alice,bob+piles[i],1) | dfs(i,j-1,alice,bob+piles[j],1);
            if temp1>temp2:
                dp[i][j]=1
                
            else:
                dp[i][j]=0
            return dp[i][j]

        if dfs(0,n-1,0,0,1):
            return True
        else:
            return False



