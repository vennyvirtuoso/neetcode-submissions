from collections import deque
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        qR=deque()
        qS=deque()
        n=len(senate)
        for i in range(len(senate)):
            if senate[i]=="R":
                qR.append(i)
            else:
                qS.append(i)

        while qR and qS:
            if qR[0]<qS[0]:
                qS.popleft()
                
                qR.append(qR[0]+n)
                qR.popleft()
            else:
                qR.popleft()
                
                qS.append(qS[0]+n)
                qS.popleft()
        if qS:
            return "Dire"
        else:
            return "Radiant"
                    