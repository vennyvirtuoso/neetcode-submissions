class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list=[[] for _ in range(numCourses)]
        taken=[]
        in_degree=[0]*numCourses
        queue = deque()

        for dep in prerequisites:
            in_degree[dep[0]]+=1
            adj_list[dep[1]].append(dep[0])
        #b->a

        for k in range(numCourses):
            if in_degree[k]==0:
                queue.append(k)
                taken.append(k)


        while queue:
            if len(taken)==numCourses:
                return taken
            course=queue.popleft()
            for deps in adj_list[course]:
                in_degree[deps]-=1
                if in_degree[deps]==0:
                    queue.append(deps)
                    taken.append(deps)



        return []