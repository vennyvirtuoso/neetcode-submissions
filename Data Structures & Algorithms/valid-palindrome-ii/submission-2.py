class Solution:
    def ispalindrome(self,s):
        # print(s)
        i=0
        j=len(s)-1
        while(i<=j):
            if s[i]!=s[j]:
                return False
            i+=1
            j-=1
        return True
    def validPalindrome(self, s: str) -> bool:
        i=0
        j=len(s)-1
        while(i<=j):
            if s[i]!=s[j]:
                a=s[:i]+s[i+1:]
                b=s[:j]+s[j+1:]
                # print(a)
                # print(b)
                if not (self.ispalindrome(a) or self.ispalindrome(b)):
                    # print(a)
                    # print("b")
                    # print(b)
                    return False
                else:
                    return True
            i+=1
            j-=1
        return True
