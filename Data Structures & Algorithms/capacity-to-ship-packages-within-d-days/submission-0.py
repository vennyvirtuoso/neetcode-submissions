class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        i=max(weights)
        j=sum(weights)
        ans=j
        while i<=j:
            mid=(i+j)//2

            day=1
            curr=0
            for weight in weights:
                curr+=weight
                # print(f'curr={curr} mid={mid}')
                if curr>mid:
                    day+=1
                    curr=weight
            # print(f'mid={mid}')
            # print(f'days={day}')
            if day>days:
                i=mid+1
            elif day<=days:
                # print(mid)
                ans=min(ans,mid)
                j=mid-1
        return ans

            
                
            
                

        print(sum)
        return 10