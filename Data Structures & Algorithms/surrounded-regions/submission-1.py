import copy
from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m=len(board)
        n=len(board[0])
        queue = deque()
        mask=copy.deepcopy(board)
        for i in [0,m-1]:
            for j in range(n):
                if board[i][j]=="O":
                    queue.append([i,j])
                    mask[i][j]="-1"
        for j in [0,n-1]:
            for i in range(m):
                if board[i][j]=="O":
                    queue.append([i,j])
                    mask[i][j]="-1"

        while queue:
            point=queue.popleft()
            directions=[(1,0),(-1,0),(0,1),(0,-1)]

            i,j=point[0],point[1]
            for di,dj in directions:
                ni,nj=i+di,j+dj
                if 0<=ni<m and 0<=nj<n and board[ni][nj]=='O' and mask[ni][nj]!="-1":
                    queue.append([ni,nj])
                    mask[ni][nj]='-1'
        for i in range(m):
            for j in range(n):
                if mask[i][j]!='-1':
                    board[i][j]='X'

        