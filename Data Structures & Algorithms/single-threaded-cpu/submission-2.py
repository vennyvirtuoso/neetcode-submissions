import heapq
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        heap=[]
        for i in range(len(tasks)):
            tasks[i].append(i)
        tasks.sort()
        # print(tasks)

        # print(tasks)
        starttime=tasks[0][0]
        index=0
        ans=[]
        lastindex=len(tasks)
        while index<lastindex:
            if tasks[index][0]<=starttime:
                heapq.heappush(heap,(tasks[index][1],tasks[index][2]))
                index+=1
            else:
                break
        while heap:
                pt,idx=heapq.heappop(heap)
                starttime+=pt
                ans.append(idx)
                while index<lastindex:
                    if tasks[index][0]<=starttime or not heap:
                        heapq.heappush(heap,(tasks[index][1],tasks[index][2]))
                        index+=1
                    else:
                        break
        return ans