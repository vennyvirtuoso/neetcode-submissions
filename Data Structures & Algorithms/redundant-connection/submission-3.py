class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def find(u):
            if parent[u]!=u:
                parent[u]=find(parent[u])

            return parent[u]
        def union(u,v):
            u = find(u)
            v = find(v)
            parent[v] = u

        n=len(edges)
        points=[i for i in range(n+1)]
        parent=[i for i in range(n+1)]

        for edge in edges:
            parent1=find(edge[0])
            parent2=find(edge[1])

            if parent1!=parent2:
                union(edge[0],edge[1])
            else:
                return edge
        
        return [0,0]
