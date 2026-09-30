class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'mountainArr') -> int:
        i=0
        n=mountainArr.length()-1
        j=n
        # mid=(i+j)//2
        mid=1
        while i<j:
            mid=(i+j)//2
            if mountainArr.get(mid)< mountainArr.get(mid+1):
                i=mid+1
            else:
                j=mid
            
        print(mid+1)
        pivot=mid+1
        i=0
        j=pivot
        while i<=j:
            mid = (i+j)//2
            if mountainArr.get(mid)==target:
                return mid
            elif mountainArr.get(mid)<target:
                i=mid+1
            else:
                j=mid-1
        i=pivot+1
        j=n
        while i<=j:
            mid = (i+j)//2
            if mountainArr.get(mid)==target:
                return mid
            elif mountainArr.get(mid)<target:
                j=mid-1
            else:
                i=mid+1
        return -1