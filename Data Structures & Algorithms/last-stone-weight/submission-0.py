import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        for i in range(len(stones)):
            stones[i]=-stones[i]
        # print(stones)
        heapq.heapify(stones)
        while len(stones)>1:
            a = -heapq.heappop(stones)
            b = -heapq.heappop(stones)
            if a < b:
                heapq.heappush(stones,-b+a)
            if a > b:
                heapq.heappush(stones,-a+b)
        if stones:
            return -stones[0]
        return 0

