class Solution:
    def mySqrt(self, x: int) -> int:
        first=1
        last=x
        ans=0
        mid=0
        while first<=last:
            mid= (first+last)//2
            # print(mid)
            if mid*mid>x:
                last=mid-1
            elif mid*mid<x:
                first=mid+1
                ans=max(ans,mid)
            else:
                return mid
        # print(last)
        # print(first)
        # if mid*mid<x:
        #     return mid
        return ans


            