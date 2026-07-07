class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # n2 = len(strs[0])
        g_long = strs[0]
        for i in range(1,len(strs)):
            longest=""
            n = len(strs[i])
            j=0
            while j<n and j<len(g_long):
                if strs[i][j]==g_long[j]:
                    longest+=strs[i][j]
                else:
                    break
                j+=1

            g_long = longest
        return g_long

                
