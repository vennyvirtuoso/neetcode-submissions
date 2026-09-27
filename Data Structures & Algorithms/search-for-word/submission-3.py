class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ans=False
        m=len(board)
        n=len(board[0])
        k=len(word)
        visited= [[0 for _ in range(n)] for _ in range(m)]
        # print(visited)
        def dfs(i,j,curr,leng):
            # print(curr)
            if curr==word:
                # print(curr)
                # print("yes") 
                nonlocal ans
                ans=True
                # return True
            elif leng<len(word)-1:
                if i-1>=0 and j>=0 and i-1<m and j<n and board[i-1][j]==word[leng+1] and visited[i-1][j]==0:
                    visited[i-1][j]=1
                    dfs(i-1,j,curr+word[leng+1],leng+1)
                    visited[i-1][j]=0
                if i+1>=0 and j>=0 and i+1<m and j<n and board[i+1][j]==word[leng+1] and visited[i+1][j]==0:
                    visited[i+1][j]=1
                    dfs(i+1,j,curr+word[leng+1],leng+1)
                    visited[i+1][j]=0
                if i>=0 and j-1>=0 and i<m and j-1<n and board[i][j-1]==word[leng+1] and visited[i][j-1]==0:
                    visited[i][j-1]=1
                    dfs(i,j-1,curr+word[leng+1],leng+1)
                    visited[i][j-1]=0
                if i>=0 and j+1>=0 and i<m and j+1<n and board[i][j+1]==word[leng+1] and visited[i][j+1]==0:
                    visited[i][j+1]=1
                    dfs(i,j+1,curr+word[leng+1],leng+1)
                    visited[i][j+1]=0
                # return False



        for i in range(m):
            for j in range(n):
                if board[i][j]==word[0]:
                    visited[i][j]=1
                    dfs(i,j,word[0],0)
                    visited[i][j]=0
        return ans