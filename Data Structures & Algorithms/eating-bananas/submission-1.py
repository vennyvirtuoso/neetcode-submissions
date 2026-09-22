import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        ans=float('inf')
        #BS
        i=1
        k=max(piles)
        while i<=k:
            mid=(i+k)//2
            # print(mid)
            hn=0
            for pile in piles:
                hn+=(math.ceil(pile/mid))
            # print(hn)
            if hn>h:
                i=mid+1
            else:
                ans=min(ans,mid)
                k=mid-1
        return ans