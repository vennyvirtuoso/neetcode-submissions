class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1=[0]*26
        count2=[0]*26
        # print(ord('a')-97)
        # return True
        for i in range(len(s1)):
            count1[ord(s1[i])-97]+=1
        j=0
        n=len(s1)
        for i in range(len(s2)):
            # count2[ord(s2[i])-65]+=1
            # if i-j<n:
            count2[ord(s2[i])-97]+=1
            if i-j+1>n:
                count2[ord(s2[j])-97]-=1
                j+=1
            if i-j+1==n:
                if count1==count2:
                    return True
        return False
            