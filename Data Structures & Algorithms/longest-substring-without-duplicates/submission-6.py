class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        check=set()
        n=len(s)
        prev=0
        curr=0
        ans=0
        for i in range(n):
            while s[i] in check:
                check.remove(s[prev])
                prev+=1
            check.add(s[i])
            ans=max(ans,i-prev+1)
        return ans  

            


