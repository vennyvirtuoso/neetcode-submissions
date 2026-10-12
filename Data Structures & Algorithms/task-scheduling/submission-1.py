class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        arr=[0]*26
        for task in tasks:
            index=ord(task)-65
            arr[index]+=1
        maxfreq=max(arr)
        k=0
        N=sum(arr)
        print(arr)
        for freq in arr:
            if freq==maxfreq:
                k+=1
        return max(N,(maxfreq-1)*(n+1)+k)
        
        # return 0