class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        csort = [0 for _ in range(30001)]
        for i in range(len(people)):
            csort[people[i]]+=1
        j=0
        for i in range(30001):
            if csort[i]>0:
                while csort[i]>0:
                    people[j]=i
                    csort[i]-=1
                    j+=1
        # print(people)
        left = 0
        right = len(people)-1

        ans=0
        while left<=right:
            if people[left]+people[right]<=limit:
                ans+=1
                left+=1
                right-=1
            else:
                ans+=1
                right-=1
        return ans