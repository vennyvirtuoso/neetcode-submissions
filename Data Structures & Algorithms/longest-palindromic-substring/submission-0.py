class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        def palindrome(center):
            left=center
            right=center

            while left>=0 and right<n and s[left]==s[right]:
                left-=1
                right+=1

            temp1=s[left+1:right]
            left=center
            right=center+1


            while left>=0 and right<n and s[left]==s[right]:
                left-=1
                right+=1
            temp2=s[left+1:right]
            return temp1 if len(temp1)>len(temp2) else temp2


        
        ans=""
        for center in range(len(s)):
            temp=palindrome(center)
            if len(temp)>len(ans):
                ans=temp
        return ans
