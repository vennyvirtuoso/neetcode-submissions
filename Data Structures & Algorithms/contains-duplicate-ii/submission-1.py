class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashh = dict()
        for i, n in enumerate(nums):
            # print(i)
            if n in hashh:
                print(i)
                pair = hashh[n]
                if abs(i-pair[0])<=k:
                    return True

            hashh[n]=[i,1]
        return False