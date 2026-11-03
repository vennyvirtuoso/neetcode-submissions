#include<functional>
class Solution {
public:
    bool isInterleave(string s1, string s2, string s3) {
        int m=s1.length();
        int n=s2.length();
        int k=s3.length();
        if (m+n!=k) return false;

        vector<vector<int>> dp(m+1, vector<int>(n+1,-1));


        function<bool(int,int)> dfs = [&](int i, int j) -> bool{
            if (i==m && j==n){
                return true;
            }
            if (dp[i][j]!=-1){
                return dp[i][j];
            }
            bool temp1=false;
            bool temp2=false;
            if (i<m && s1[i]==s3[i+j]){
                temp1=dfs(i+1,j);
            }
            if (j<n && s2[j]==s3[i+j]){
                temp2=dfs(i,j+1);
            }
            dp[i][j]=temp1 | temp2;
            return dp[i][j];
        };
        return dfs(0,0);


    }
};
