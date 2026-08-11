class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        fq= {}
        for num in nums:
            fq[num]= fq.get(num,0)+1
        # print(fq)
        bucket = [[] for _ in range(10001)]
        for key in fq:
            freq=fq[key]
            bucket[freq].append(key)
        ans=[]
        for i in range(10000,-1,-1):
            for num in bucket[i]:
                if k>0:
                    ans.append(num)
                    k=k-1
        return ans