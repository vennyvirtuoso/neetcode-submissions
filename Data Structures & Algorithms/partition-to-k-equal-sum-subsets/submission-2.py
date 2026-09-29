class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False
        req = total // k
        nums.sort(reverse=True)
        bucket = [0] * k
        n = len(nums)

        def dfs(index):
            if index == n:
                return True
            seen = set()
            for i in range(k):
                if bucket[i] in seen:
                    continue
                seen.add(bucket[i])
                if bucket[i] + nums[index] <= req:

                    bucket[i] += nums[index]

                    if dfs(index + 1):
                        return True
                    bucket[i] -= nums[index]
                    if bucket[i] == 0:
                        break

            return False

        return dfs(0)