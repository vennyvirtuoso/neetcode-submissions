"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start=[]
        end=[]
        for interval in intervals:
            start.append(interval.start)
            end.append(interval.end)

        start.sort()
        end.sort()
        print(start)
        print(end)
        count=0
        i=0
        j=0
        ans=0
        while i<len(start):
            if start[i]<end[j]:
                ans=max(ans,count)
                count+=1
                i+=1
            else:
                ans=max(ans,count)
                count-=1
                # i+=1
                j+=1
            ans=max(ans,count)

        return ans
            
