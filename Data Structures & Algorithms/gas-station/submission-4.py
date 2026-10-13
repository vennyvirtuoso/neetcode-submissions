class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        for i in range(len(gas)):
            gas[i]=gas[i]-cost[i]

        index=0
        currsum=0
        for i in range(len(gas)):
            currsum+=gas[i]
            if currsum<0:
                currsum=0
                index=i+1
        if sum(gas)<0:
            return -1
        return index


        