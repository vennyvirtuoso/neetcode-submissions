class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        check=set()
        n=len(s)
        if n==0:
            return 0
        prev=0
        check.add(s[prev])
        curr=1
        
        ans=1
        while curr<n and prev<=curr:
            if s[curr] not in check:
                check.add(s[curr])
                curr+=1
                
            else:
                while s[curr] in check:
                    if s[prev] in check:
                        check.remove(s[prev])
                    prev+=1
            ans=max(ans, curr-prev)
        return ans

