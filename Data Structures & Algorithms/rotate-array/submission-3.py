class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        k=k%n
        nums.reverse()
        mid = (k-1)//2
        last = k-1
        start=0
        while start<=mid:
            nums[start],nums[last]=nums[last], nums[start]
            last-=1
            start+=1
        mid = (k+n-1)//2
        last = n-1
        start=k
        # print(mid)
        while start<=mid:
            # print(start)
            # print(last)
            nums[start],nums[last]=nums[last], nums[start]
            last-=1
            start+=1
        

