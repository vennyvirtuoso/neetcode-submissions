class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        track=dict()
        for i in range(len(s)):
            if s[i] in track:
                track[s[i]].append(i)
            else:
                track[s[i]]=[i]

        # print(track)
        ans=[]
        i=0
        while i<len(s):
            ch = s[i]
            rang=track[s[i]][-1]
            j=i
            while j<=rang:
                rang=max(rang,track[s[j]][-1])
                j+=1
            ans.append((rang-i+1))
            i=rang+1


        return ans
        