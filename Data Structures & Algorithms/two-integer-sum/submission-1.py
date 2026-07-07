class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            value2 = target-nums[i]
            for j in range(i+1,n):
                if nums[j]==value2:
                    return [i,j]