class Solution {
public:
    bool stoneGame(vector<int>& piles) {
        int n = piles.size();
        vector<vector<int>> dp(n,vector<int>(n,-1));
        function<int(int,int,int,int,bool)> dfs=[&](int i,int j, int alice,int bob,bool turn)-> int{
            if (i>j){
                return alice>bob;
            }
            if (dp[i][j]!=-1){
                return dp[i][j];
            }
            int temp1=-1;int temp2=-1;
            if (turn ==true){
                temp1 = dfs(i+1,j,alice+piles[i],bob,0) | dfs(i,j-1,alice+piles[j],bob,0);
            }
            else{
                temp2 = dfs(i+1,j,alice,bob+piles[i],0) | dfs(i,j-1,alice,bob+piles[j],0);
            }
            if (temp1>temp2){
                dp[i][j]=1;
            }
            else{
                dp[i][j]=0;
            }
            return dp[i][j];
        };
        dfs(0,n-1,0,0,1);
        if (dp[0][n-1]==1){
            return true;
        }
        else{
            return false;
        }
    }
};