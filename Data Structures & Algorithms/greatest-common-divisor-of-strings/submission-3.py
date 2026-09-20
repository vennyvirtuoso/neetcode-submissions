class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        n1,n2 = len(str1),len(str2)
        if n1>n2:
            n1,n2=n2,n1
        while(n1):
            n2,n1=n1,n2%n1
        # print(n2)
        length=1
        gcd=n2
        # print(gcd)
        n1,n2 = len(str1),len(str2)
        # for i in range(gcd, length-1,-1):
        
        if str1[0:gcd]*(n1//gcd)==str1 and str2[0:gcd]*(n2//gcd)==str2:
            if str1[0:gcd]==str2[0:gcd]:
                return str1[0:gcd] 
            else:
                return ""
        return ""