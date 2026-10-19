from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        queue=deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j]==2:
                    queue.append([i,j])
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        ans=0

        while queue:
            length=len(queue)

            for k in range(length):
                point=queue.popleft()
                i,j=point[0],point[1]

                for di,dj in directions:

                    ni,nj=i+di,j+dj

                    if 0<=ni<m and 0<=nj<n:
                        if grid[ni][nj]==1:
                            
                            grid[ni][nj]=2
                            queue.append([ni,nj])
            if queue:
                ans+=1
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    return -1

        return ans
