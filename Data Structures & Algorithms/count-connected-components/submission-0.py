from collections import deque
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list=[[] for _ in range(n)]

        for edge in edges:
            adj_list[edge[0]].append(edge[1])
            adj_list[edge[1]].append(edge[0])

        visited=[0]*n
        count=0
        for i in range(n):
            if visited[i]==0:
                count+=1
                queue=deque()
                queue.append(i)
                visited[i]=1

                while queue:
                    point=queue.popleft()

                    connect=adj_list[point]
                    for con in connect:
                        if not visited[con]:
                            visited[con]=1
                            queue.append(con)
            else:
                continue
        return count
