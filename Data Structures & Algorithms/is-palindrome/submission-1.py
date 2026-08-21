class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        i=0
        j=n-1
        while(i<(n//2) and j>=(n//2)):
            if s[i].isalnum() and s[j].isalnum():
                # print("both")
                if s[i].lower()!=s[j].lower():
                    return False
                i+=1
                j-=1
            if not s[i].isalnum():
                # print("inot")
                i+=1
            if not s[j].isalnum():
                # print("jnot")
                j-=1
            

        return True