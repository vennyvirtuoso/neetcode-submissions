class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n1=len(a)-1
        n2=len(b)-1
        carry=0
        ans=""
        while n1>=0 or n2>=0:
            temp1=0
            temp2=0

            if n2>=0:
                temp2=int(b[n2])
            if n1>=0:
                temp1=int(a[n1])
            if temp2+temp1+carry==3:
                ans="1"+ans
                carry=1
            elif temp2+temp1+carry==2:
                ans="0"+ans
                carry=1
            elif temp2+temp1+carry==1:
                ans="1"+ans
                carry=0
            elif temp2+temp1+carry==0:
                ans="0"+ans
                carry=0
            n1-=1
            n2-=1
        if carry==1:
            ans="1"+ans
        return ans



