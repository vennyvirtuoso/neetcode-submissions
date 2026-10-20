from collections import deque
import copy
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends=set(deadends)
        if "0000" in deadends:
            return -1
        queue=deque()
        visited=set()
        queue.append("0000")
        visited.add("0000")
        steps=0
        while queue:
            length=len(queue)
            for k in range(length):
                state=queue.popleft()
                if state==target:
                    return steps
                for i in range(4):
                    near1=copy.deepcopy(state)
                    near2=copy.deepcopy(state)
                    near1=list(near1)
                    near2=list(near2)
                    near1[i]=str((int(state[i])+1)%10)
                    
                    near2[i]=str((int(state[i])-1)%10)
                    near1="".join(near1)
                    near2="".join(near2)
                    if near1 not in visited and near1 not in deadends:
                        queue.append(near1)
                        visited.add(near1)
                    if near2 not in visited and near2 not in deadends:
                        queue.append(near2)
                        visited.add(near2)
            steps+=1
        return -1
