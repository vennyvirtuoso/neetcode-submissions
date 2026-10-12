import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        heap=[]
        freq=dict()
        for strr in s:
            freq[strr]=freq.get(strr,0)+1
        # print(freq)
        for key,fq in freq.items():
            heapq.heappush(heap,(-fq,key))
        prev=["",0]
        ans=""
        while heap:
            # print(heap)
            fq,curr = heapq.heappop(heap)
            if prev[0]=="":
                prev[0]=curr
                prev[1]=-fq-1
                ans+=curr
            elif prev[0]==curr:
                return ""
            else:
                if prev[1]>0:
                    heapq.heappush(heap,(-prev[1],prev[0]))
                prev[0]=curr
                prev[1]=-fq-1
                ans+=curr


        # print(ans)
        if len(ans)<len(s):
            return ""
        else:
            return ans
