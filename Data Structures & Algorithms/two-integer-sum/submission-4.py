class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        dictt=dict()
        for i in range(n):
            value2 = target-nums[i]
            if value2 in dictt.keys():
                indexs = dictt[value2]
                return [indexs,i]

            else:
                dictt[nums[i]]=i
