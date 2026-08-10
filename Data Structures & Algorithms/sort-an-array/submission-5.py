
def quicksort(low,high,nums):
    if low<high:
        pivot = nums[((low+high)//2)]
        i=low
        j=high
        while i<=j:
            while nums[i]<pivot:
                i=i+1
            while nums[j]>pivot:
                j=j-1
            if i<=j:
                nums[i], nums[j] = nums[j], nums[i]
                i=i+1
                j=j-1

        quicksort(low,j,nums)
        quicksort(i,high,nums)
    else:
        return   

    

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # selection sort
        n = len(nums)
        quicksort(0,n-1,nums)
        return nums
        