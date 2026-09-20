class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        start=[0]*8
        start[0]=26
        for i in range(1,8):
            start[i]=start[i-1]+26**(i+1)
        index=0
        # print(start)
        for i in range(1,8):
            if start[i]>=columnNumber and start[i-i]<columnNumber:
                index= i
                break
        ans=""
        # print(index)
        while index>=0:
            multi = columnNumber//(26**index)
            # print(multi)
            if multi>26:
                multi=26
            # print(multi)
            ch = chr(ord('A')+multi-1)
            ans+=ch
            columnNumber-=multi*(26**index)
            index-=1
        return ans
            