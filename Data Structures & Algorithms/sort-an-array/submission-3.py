def merge(i,mid,j,nums):
    m = j-i+1
    temp_arr = [0 for _ in range(m)]
    x=i
    y=mid+1
    k=0
    while x<=mid and y<=j:
        if nums[x]<=nums[y]:
            temp_arr[k]=nums[x]
            k=k+1
            x=x+1
        else:
            temp_arr[k]=nums[y]
            y=y+1
            k=k+1
    while x<=mid:
        temp_arr[k]=nums[x]
        k=k+1
        x=x+1
    while y<=j:
        temp_arr[k]=nums[y]
        y=y+1
        k=k+1
    k=0
    for z in range(i,j+1):
        nums[z]=temp_arr[k]
        k=k+1


def mergesort(i,j,nums):
    if i<j:
        mid = (i+j)//2
        mergesort(i,mid,nums)
        mergesort(mid+1,j,nums)
        merge(i,mid,j,nums)
    else:
        return 
    

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # selection sort
        n = len(nums)
        mergesort(0,n-1,nums)
        return nums
        