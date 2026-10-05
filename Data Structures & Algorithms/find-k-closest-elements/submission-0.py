class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        i=0
        j=len(arr)-1
        while i<=j:
            mid=(i+j)//2
            if arr[mid]<x:
                i=mid+1
            elif arr[mid]>=x:
                j=mid-1
            else:
                break
        left=i-1
        right=i
        n=len(arr)
        while right-left-1<k:
            if left<0:
                right+=1
            elif right>=n:
                left-=1
            elif abs(arr[left] - x) <= abs(arr[right] - x):
                left-=1
            else:
                right+=1
        return arr[left+1:right]