import heapq
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        def compare(x):
            return x[1]
        trips.sort(key=compare)
        currcp=0
        heap=[]
        for cp,start,end in trips:
            while heap and heap[0][0]<=start:
                currcp-=heap[0][1]
                heapq.heappop(heap)
            currcp+=cp
            if currcp>capacity:
                return False
            heapq.heappush(heap,(end,cp))
        return True
                
