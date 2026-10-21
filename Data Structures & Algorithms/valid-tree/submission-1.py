from collections import deque 
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges)!=n-1:
            return False
        adj_list=[[] for _ in range(n)]
        queue=deque()
        for edge in edges:
            adj_list[edge[0]].append(edge[1])
            adj_list[edge[1]].append(edge[0])
        visited=[0]*n
        queue.append([0,-1])
        visited[0]=1
        while queue:
            node=queue.popleft()
            nodes=adj_list[node[0]]

            for n in nodes:
                if visited[n]==0:
                    queue.append([n,node[0]])
                    visited[n]=1
                elif visited[n]==1 and n!=node[1]:
                    return False
        return all(visited)



