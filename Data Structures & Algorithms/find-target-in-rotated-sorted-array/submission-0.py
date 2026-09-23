class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def binarys(nums,i,j,target):
            # print(i)
            # print(j)
            while i<=j:
                mid=(i+j)//2
                if target<nums[mid]:
                    j=mid-1
                elif target>nums[mid]:
                    i=mid+1
                else:
                    return mid
            return -1
        i = 0
        j = len(nums) - 1
        n=j+1
        while i < j:
            mid = (i + j) // 2
            if nums[mid] > nums[j]:
                i = mid + 1
            else:
                j = mid

        pivot = i
        # print(pivot)
        index1=binarys(nums,0,pivot-1,target)
        index2=binarys(nums,(pivot),n-1,target)
        # print(index1)
        # print(index2)
        if index1<0 and index2<0:
            return -1
        else:
            return max(index1,index2)



