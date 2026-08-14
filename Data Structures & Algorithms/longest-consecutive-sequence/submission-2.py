class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        listunique = set(nums)
        ans = 0
        # print(listunique)
        for num in listunique:
            length = 1
            check = num+1
            # listunique.remove(num)
            if num-1 not in listunique:

                while check in listunique:
                    length+=1
                    check+=1
                    # listunique.remove(check)
            ans = max(ans,length)

        return ans