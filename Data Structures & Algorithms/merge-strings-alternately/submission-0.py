class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len1=len(word1)
        len2=len(word2)
        i=0
        j=0
        ans=""
        while i<len1 and j<len2:
            ans+=word1[i]
            ans+=word2[j]
            i+=1
            j+=1
        while i<len1:
            ans+=word1[i]
           
            i+=1

        while j<len2:

            ans+=word2[j]

            j+=1
        return ans
