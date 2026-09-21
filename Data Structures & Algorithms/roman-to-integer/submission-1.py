class Solution:
    def romanToInt(self, s: str) -> int:
        ans=0
        dictt = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        i=len(s)-1
        while i>=1:
            curr = s[i]
            prev=s[i-1]
            if dictt[prev]<dictt[curr]:
                ans+=dictt[curr]
                ans-=dictt[prev]
                i-=1
            else:
                ans+=dictt[curr]
            i-=1
        if len(s)>1:
            if not (dictt[s[0]]<dictt[s[1]]):
                ans+=dictt[s[0]]
        else:
            ans+=dictt[s[0]]
        return ans

