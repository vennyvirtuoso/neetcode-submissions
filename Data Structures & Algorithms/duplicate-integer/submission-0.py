class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique = set()
        for num in nums:
            unique.add(num)
        if len(unique)<len(nums):
            return True
        else:
            return False