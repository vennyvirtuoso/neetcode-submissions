class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        ans=0
        intervals.sort(key=lambda x: x[0])
        n=len(intervals)
        newIntervalE=intervals[0][1]
        # print(intervals)
        for i in range(1,n):
            curr=intervals[i]

            if curr[0]>=newIntervalE:
                
                newIntervalE=curr[1]
                continue
            else:
                ans+=1
                # newInterval[0]=min(newInterval[0],curr[0])
                newIntervalE=min(newIntervalE,curr[1])
        # ans.append(newInterval)

        return ans