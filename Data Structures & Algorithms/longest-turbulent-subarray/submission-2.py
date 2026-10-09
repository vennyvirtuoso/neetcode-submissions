class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        first=False
        second=False
        i=0
        n=len(arr)
        ans=1
        while i<n-1:

            if arr[i]>arr[i+1]:
                k=i
                i+=1
                turn=False
                while i<n-1:
                    if arr[i]>arr[i+1] and turn:
                        turn=False
                        i+=1
                    elif arr[i]<arr[i+1] and not turn:
                        turn=True
                        i+=1
                    else:
                        break
                ans=max(ans,i-k+1)
            elif arr[i]<arr[i+1]:
                k=i
                i+=1
                turn=False
                while i<n-1:
                    if arr[i]<arr[i+1] and turn:
                        turn=False
                        i+=1
                    elif arr[i]>arr[i+1] and not turn:
                        turn=True
                        i+=1
                    else:
                        break
                ans=max(ans,i-k+1)
            else:
                i+=1
        
        return ans
