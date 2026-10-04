class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = [0]*26
        maxfreq=0
        n=len(s)
        ans=0
        # print(ord('Z')-65)
        j=0
        for i in range(n):
            count[ord(s[i])-65]+=1
            maxfreq=max(count)
            if (i-j+1)-maxfreq<=k:
                ans=max(ans,i-j+1)
            else:
                while (i-j+1)-maxfreq>k:
                    count[ord(s[j])-65]-=1
                    j+=1
                    maxfreq=max(count)
        return ans
