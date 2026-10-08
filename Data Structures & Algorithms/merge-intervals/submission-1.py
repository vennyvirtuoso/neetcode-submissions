class Solution:

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        def compare(x):
            return x[0]<x[1]
        ans=[]
        intervals.sort()
        n=len(intervals)
        newInterval=intervals[0]
        # print(intervals)
        for i in range(1,n):
            curr=intervals[i]

            if curr[0]>newInterval[1]:
                ans.append(newInterval)
                newInterval=curr
                continue
            else:
                newInterval[0]=min(newInterval[0],curr[0])
                newInterval[1]=max(newInterval[1],curr[1])
        ans.append(newInterval)

        return ans
        