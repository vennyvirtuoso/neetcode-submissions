class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        ans=0
        intervals.sort()
        n=len(intervals)
        newInterval=intervals[0]
        # print(intervals)
        for i in range(1,n):
            curr=intervals[i]

            if curr[0]>=newInterval[1]:
                
                newInterval=curr
                continue
            else:
                ans+=1
                # newInterval[0]=min(newInterval[0],curr[0])
                newInterval[1]=min(newInterval[1],curr[1])
        # ans.append(newInterval)

        return ans