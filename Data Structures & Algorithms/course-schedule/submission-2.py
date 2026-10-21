from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list=[[] for _ in range(numCourses)]
        taken=0
        in_degree=[0]*numCourses
        queue = deque()

        for dep in prerequisites:
            in_degree[dep[0]]+=1
            adj_list[dep[1]].append(dep[0])
        #b->a

        for k in range(numCourses):
            if in_degree[k]==0:
                queue.append(k)
                taken+=1


        while queue:
            if taken==numCourses:
                return True
            course=queue.popleft()
            for deps in adj_list[course]:
                in_degree[deps]-=1
                if in_degree[deps]==0:
                    queue.append(deps)
                    taken+=1



        return False
