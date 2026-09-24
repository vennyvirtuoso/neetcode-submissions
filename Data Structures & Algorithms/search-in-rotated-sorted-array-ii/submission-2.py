class Solution:
    def search(self, nums: List[int], target: int) -> bool:

        n=len(nums)
        i=0
        j=n-1
        while i<=j:
            mid=(i+j)//2
            if nums[mid]==target:
                return True
            elif nums[mid]==nums[i]==nums[j]:
                i+=1
                j-=1
            elif nums[i]==nums[mid] :
                i+=1
            elif nums[mid]==nums[j]:
                j-=1
            elif nums[i]<nums[mid]:
                if nums[i]<=target<nums[mid]:
                    j=mid-1
                else:
                    i=mid+1
            elif nums[mid]<nums[j]:
                if nums[mid]<target<=nums[j]:
                    i=mid+1
                else:
                    j=mid-1
        return False