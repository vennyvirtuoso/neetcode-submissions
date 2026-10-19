from collections import deque
import copy
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific=set()
        atlantic=set()
        p_grid=copy.deepcopy(heights)
        m=len(p_grid)
        n=len(p_grid[0])
        queue=deque()
        for i in range(m):
            for j in range(n):
                if i==0 or j==0:
                    p_grid[i][j]=-1
                    queue.append([i,j])
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        while queue:
            length=len(queue)

            for k in range(length):
                point=queue.popleft()
                i,j=point[0],point[1]

                for di,dj in directions:
                    ni,nj=i+di,j+dj
                    if 0<=ni<m and 0<=nj<n and p_grid[ni][nj]!=-1 and heights[ni][nj]>=heights[i][j]:
                        queue.append([ni,nj])
                        p_grid[ni][nj]=-1
        
        for i in range(m):
            for j in range(n):
                if p_grid[i][j]==-1:
                    pacific.add((i,j))



        a_grid=copy.deepcopy(heights)
        m=len(a_grid)
        n=len(a_grid[0])
        queue=deque()
        for i in range(m):
            for j in range(n):
                if i==m-1 or j==n-1:
                    a_grid[i][j]=-1
                    queue.append([i,j])
        directions=[(1,0),(-1,0),(0,1),(0,-1)]

        while queue:
            length=len(queue)

            for k in range(length):
                point=queue.popleft()
                i,j=point[0],point[1]

                for di,dj in directions:
                    ni,nj=i+di,j+dj
                    if 0<=ni<m and 0<=nj<n and a_grid[ni][nj]!=-1 and heights[ni][nj]>=heights[i][j]:
                        queue.append([ni,nj])
                        a_grid[ni][nj]=-1
        
        for i in range(m):
            for j in range(n):
                if a_grid[i][j]==-1:
                    atlantic.add((i,j))
        return list(pacific & atlantic)
        

        