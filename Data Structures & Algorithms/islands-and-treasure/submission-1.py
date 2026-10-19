from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        queue=deque()
        m=len(grid)
        n=len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j]==0:
                    queue.append([i,j,0])
        
        while queue:
            length= len(queue)

            for k in range(length):
                point=queue.popleft()
                i=point[0]
                j=point[1]
                d=point[2]
                if i-1>=0 and j>=0 and i-1<m and j<n:
                    if grid[i-1][j]==2147483647:
                        queue.append([i-1,j,d+1])
                        grid[i-1][j]=d+1
                if i+1>=0 and j>=0 and i+1<m and j<n:
                    if grid[i+1][j]==2147483647:
                        queue.append([i+1,j,d+1])
                        grid[i+1][j]=d+1
                if i>=0 and j-1>=0 and i<m and j-1<n:
                    if grid[i][j-1]==2147483647:
                        queue.append([i,j-1,d+1])
                        grid[i][j-1]=d+1
                if i>=0 and j+1>=0 and i<m and j+1<n:
                    if grid[i][j+1]==2147483647:
                        queue.append([i,j+1,d+1])
                        grid[i][j+1]=d+1


        