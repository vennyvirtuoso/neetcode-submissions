class Solution:
    def checkValidString(self, s: str) -> bool:
        high=0
        low=0

        for i in range(len(s)):
            if s[i]=="(":
                high+=1
                low+=1

            elif s[i]=="*":
                high+=1
                low-=1
            elif s[i]==")":
                high-=1
                low-=1
            if high<0:
                return False
            low=max(low,0)

        return low==0