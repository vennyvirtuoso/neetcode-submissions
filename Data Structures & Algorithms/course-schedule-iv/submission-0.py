from collections import deque
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj_list=[[] for _ in range(numCourses)]
        ans=[]
        for pair in prerequisites:
            adj_list[pair[0]].append(pair[1])
        
        def dfs(query):
            queue=deque()
            queue.append(query[0])
            visited=[0]*numCourses
            visited[query[0]]=1
            while queue:
                course=queue.popleft()

                deps=adj_list[course]

                if query[1] in deps:
                    return True
                
                else:
                    for dep in deps:
                        if visited[dep]==0:
                            queue.append(dep)
                            visited[dep]=1
            return False

        for query in queries:
            ans.append(dfs(query))
        return ans