class Solution:
    def findMin(self, nums: List[int]) -> int:
        i=0
        j=len(nums)-1
        n=j+1
        ans=float('inf')
        while i<=j:
            mid=(i+j)//2
            # print(i)
            # print(j)
            # print(mid)
            ans=min(ans,nums[mid%n])
            # print(ans)
            if not nums[i]<=nums[mid]:
                j=mid-1
            elif not nums[mid]<=nums[j]:
                # print(i)
                i=mid+1
            else:
                break
        # print(i)
        ans=min(ans,nums[i])
        return ans