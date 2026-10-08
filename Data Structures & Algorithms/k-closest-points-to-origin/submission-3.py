import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap= [(abs(point[0])*abs(point[0])+abs(point[1]*abs(point[1])),point) for point in points]
        # print(heap)
        heapq.heapify(heap)
        size=len(points)
        size=size-k
        # for i in range(k):
        #     heapq.heappop(heap)
        ans=[]
        for i in range(k):
            ans.append((heapq.heappop(heap)[1]))
        return ans