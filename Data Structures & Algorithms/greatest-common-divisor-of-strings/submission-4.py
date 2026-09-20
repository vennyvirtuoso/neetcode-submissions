import math
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        n1,n2 = len(str1),len(str2)
        
        g=math.gcd(n1,n2)
        for i in range(n1):
            if str1[i]!=str2[i%g]:
                return ""
        for i in range(n2):
            if str2[i]!=str1[i%g]:
                return ""
        return str1[:g]
